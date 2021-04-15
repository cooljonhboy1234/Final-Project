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
Start-Process py -ArgumentList ".\Final_Project_Script.py" -NoNewWindow -wait

#This function is to let you see if the image of the day 
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

   #removes any prevouis background set
     Remove-ItemProperty -path "HKCU:\Control Panel\Desktop" -name WallPaper      
   #sets a new background to the image            
     set-itemproperty -path "HKCU:\Control Panel\Desktop" -name WallPaper -value $ApodImage
      

Sleep -seconds 1

     RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True


         Get-ItemProperty -path "HKCU:\Control Panel\Desktop" 
}

#Start-Process powershell -ArgumentList "-file C:\Users\jonna\OneDrive\Desktop\scripting APP\Final Project\cache\SQL_Script.py"

#getting newest image of the day
$NewestImage = Get-ChildItem -Path 'C:\Users\jonna\OneDrive\Desktop\scripting APP\Final Project\cache' -Filter '*.jpg?' | sort LastWriteTime | select -last 1 

#setting the path to newest image of the day
$PathTo = Join-Path -Path 'C:\Users\jonna\OneDrive\Desktop\scripting APP\Final Project\' -ChildPath $NewestImage

#Recall function made earlier.
Set-WallPaper -ApodImage $PathTo

#Fixed issues with Rundll32.exe not refershing by just inserting it again after 
sleep -Seconds 1 | RUNDLL32.EXE USER32.DLL,UpdatePerUserSystemParameters ,1 ,True



