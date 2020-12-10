<#
.SYNOPSIS: The windows host is an AWS EC2 instance having xyz ARN. Schedule this Script on Task scheduler for every 1 minute interval. 
It will check the Service status and post the same to Cloudwatch metrics. It will also create Cloudwatch Alarm if the Windows service is found in stopped state.

.PARAMETER: SNSTopicARN
SNSTopicARN is mandatory parameter to create CloudWatch Alarms. To execute the script a valid ARN needs to be
created and used as a parameter.
#>
[CmdletBinding()]
Param(
    # Provide Topic ARM
    [string]$SNSTopicArn = 'xyz' #write your ARN here
)

##Write Metric Data to CloudWatch
Import-Module -Name AWSPowerShell
$namespace = "My first Windows service CLoudwatch Metrics"

$instance_MetaData = Invoke-RestMethod -Uri http://169.254.169.254/latest/dynamic/instance-identity/document
$region = $Instance_Metadata.region
$instance_Id = $Instance_Metadata.instanceId
$instance_Name = $env:COMPUTERNAME

#logging
$date_UTC = (Get-Date).ToUniversalTime()
$log_Folder_Path = ([environment]::getfolderpath("WINDOWS")).split("\")[0] + "\CW-QF-MonitoringDONOTDELETE"
$log_Path = -join($log_Folder_Path, "\PostToCWLogs")

if(-not (Test-Path $log_Path))
{
    New-Item -Path $log_Path -ItemType directory | Out-Null
}
else
{
    Get-ChildItem -Path $log_Path | Where-Object {$_.LastWriteTime -le (Get-Date).AddHours(-3)} | Remove-Item -Recurse -Force | Out-Null
}
$log_File_Name = "PushToCW-" + (Get-Date -Format "dd-MMM-yyyy-hh-mm-ss") + ".log"
$log_File_Path = -join($log_Path,"\",$log_File_Name)

#Fucntion to Write Metrics to Cloudwatch
Function Write-MetricDataToCloudWatch {
    Param(
        [string]$CounterName,
        [string]$MetricName,
        [string]$Unit
    )

    ### Upload Service status Counter Data into Cloudwatch
    try{
        ##Dimension1
        $Dimension1 = New-Object Amazon.CloudWatch.Model.Dimension
        $Dimension1.set_Name("InstanceId")
        $Dimension1.set_Value("$instance_Id")
        ##Dimension2
        $Dimension2 = New-Object Amazon.CloudWatch.Model.Dimension
        $Dimension2.set_Name("InstanceName")
        $Dimension2.set_Value("$instance_Name")
        ##Dimension3
        $Dimension3 = New-Object Amazon.CloudWatch.Model.Dimension
        $Dimension3.set_Name("$MetricName")
        $Dimension3.set_Value("Count")
        ##MetricDatum 
        $Dat = New-Object Amazon.CloudWatch.Model.MetricDatum
        $Dat.Timestamp = $date_UTC
        $Dat.MetricName = $MetricName
        $Dat.Unit = "Count"
        
        # Windows Service = any windows service for which you want to upload the Cloudwatch metrics
        if((Get-Service "Windows Service").status -eq "Running"){
            
            $Dat.Value = 1
        }
        else{
            $Dat.Value = 0
        }
       
        $Dat.Dimensions.Add($Dimension1)
        $Dat.Dimensions.Add($Dimension2)
        $Dat.Dimensions.Add($Dimension3)
        
        Write-CWMetricData -Namespace $namespace -MetricData $Dat -region $region

        "$(Get-Date -Format "dd-MMM-yyyy-hh-mm-ss") ::: $($Dimension1.Name) = $($Dimension1.Value)`t$($Dimension2.Name) = $($Dimension2.Value)`t$($Dimension3.Name) = $($Dimension3.Value)" | Out-File $log_File_Path -Append
        "$(Get-Date -Format "dd-MMM-yyyy-hh-mm-ss") ::: $($Dat.MetricName) $($Dat.Value) $($Dat.Unit)" | Out-File $log_File_Path -Append


        # Specify Parameters
        $params = @{
            "AlarmName" = -join($instance_Name, "-", $Dat.MetricName)
            "AlarmDescription" = -join($Service, "-", "Service-Status")
            "ActionsEnabled" = $true
            "AlarmAction" = $SNSTopicArn
            "ComparisonOperator" = "LessThanThreshold"
            "Dimensions" = $Dat.Dimensions
            "EvaluationPeriod" = 1
            "MetricName" = $Dat.MetricName
            "Namespace" = $namespace
            "Period" = 60
            "Statistic" = "Average"
            "Threshold" = 1
            "Unit" = "Count"
        }
    
        # Create Rule
        if(Get-CWAlarm -AlarmName $params.AlarmName -Region $region){
            "$(Get-Date -Format "dd-MMM-yyyy-hh-mm-ss") ::: $($params.AlarmName) ::: Alarm Already Exists" | Out-File $log_File_Path -Append
        }
        else{
            Write-CWMetricAlarm @params -Region $region
            "$(Get-Date -Format "dd-MMM-yyyy-hh-mm-ss") ::: $($params.AlarmName) ::: Alarm Created" | Out-File $log_File_Path -Append
        }
    
        $Dat = $null
        $Dimension1 = $null
        $Dimension2 = $null
        $Dimension3 = $null
        $params = $null
    }
    catch{
        $PSItem.Exception.Message | Out-File $log_File_Path -Append
    }
}

$MetricName = "Windows Service Status"
Write-MetricDataToCloudWatch -MetricName $MetricName -Unit $Unit

"$(Get-Date -Format "dd-MMM-yyyy-hh-mm-ss") ::: Metrics Uploaded to CloudWatch Script Completed Successfully" | Out-File $log_File_Path -Append
