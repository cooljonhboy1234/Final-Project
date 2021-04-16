#.-- .... -.-- / ..- / -- .- -.- . / -- . / -.-. --- -- -- . -. -
# Description:
#    Takes images from Final script that were download most recently
#    and sets it to the computers background. Side note, Run this 
#    script since its going to be the parent to the other scripts
#    made in python.
# Usage: RUN_THIS.ps1
#   
#
#    
#.-- .... -.-- / ..- / -- .- -.- . / -- . / -.-. --- -- -- . -. -


#This function is to let you see if the image of the day has been properly setup in wallpaper inside th HKCU registry.
function Test-RegistryValue {

param (

 [parameter(Mandatory=$true)]
 [ValidateNotNullOrEmpty()]$Path,

[parameter(Mandatory=$true)]
 [ValidateNotNullOrEmpty()]$Value
)

try {

Get-ItemProperty -Path $Path | Select-Object -ExpandProperty $Value -ErrorAction Stop | Out-Null
 return $true
 }

catch {

return $false

}

}

#function chages background of desktop
function Set-WallPaper ($ApodImage)
{
Write-Output "10 seconds for the code to finish running, please be patient."
Sleep -seconds 1
   #removes any background perviously 
     Remove-ItemProperty -path "HKCU:\Control Panel\Desktop" -name WallPaper     
   #sets a new background to the image            
     set-itemproperty -path "HKCU:\Control Panel\Desktop" -name WallPaper -value $ApodImage
      
Sleep -seconds 5
    #update to our rundll32 problem, if it is repeated multiple times it will force the background to chage i.e. PROBLEM SOLVED!
    for ($i = 0; $i -le 20; $i++)
    {
        RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True
    }
     


         Get-ItemProperty -path "HKCU:\Control Panel\Desktop" 
}

$days = Read-Host -Prompt 'How many days would you like the code to run'

Write-Output "Mark the time since the code will run in the next 24h again."

#This is the loop to do the script at a selected time
for ($i = [int]$days; $i -ge 0; $i-- )
{
    Write-Output "The current time running code at: " 
    Get-Date 
    #Creating SQL database if it doesn't exists
    Start-Process py -ArgumentList ".\SQL_Script.py"
    #Runnes download image script before setting it to the background.
    Start-Process py -ArgumentList ".\Final_Project_Script.py" -NoNewWindow -wait

    #getting newest image of the day
    $NewestImage = Get-ChildItem -Path '.\' -Filter '*.jpg?' | sort LastWriteTime | select -last 1 

    #setting the path to newest image of the day
    $PathTo = Join-Path -Path 'C:\Users\jonna\OneDrive\Desktop\scripting APP\Final Project\cache' -ChildPath $NewestImage

    #Recall function made earlier.
    Set-WallPaper -ApodImage $PathTo

    #logging script activates after everythings has been ran.
    Start-Process py -ArgumentList ".\Log_Script.py" -NoNewWindow -wait

    Write-Output "Remaining days left tell code stops: " $i" Days left till script stops. (Force Stop Crtl+C)"
    if ($i -eq '0')
    {
       Write-Output "Script has finished Running"
    }
    else
    {
         sleep -Seconds 86400
    }
}




