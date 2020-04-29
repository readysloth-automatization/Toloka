param([switch]$Elevated)

function Test-Admin {
  $currentUser = New-Object Security.Principal.WindowsPrincipal $([Security.Principal.WindowsIdentity]::GetCurrent())
  $currentUser.IsInRole([Security.Principal.WindowsBuiltinRole]::Administrator)
}

if ((Test-Admin) -eq $false)  {
    if ($elevated)
    {
        # tried to elevate, did not work, aborting
    }
    else {
        Start-Process powershell.exe -Verb RunAs -ArgumentList ('-noprofile -noexit -file "{0}" -elevated' -f ($myinvocation.MyCommand.Definition))
}

exit
}

[Net.ServicePointManager]::SecurityProtocol = [Net.SecurityProtocolType]::Tls12;

(New-Object System.Net.WebClient).DownloadFile('https://www.python.org/ftp/python/3.8.2/python-3.8.2.exe', 'C:\Windows\Temp\python_installer.exe')


C:\Windows\Temp\python_installer.exe | Out-Null
py -3 -m pip install wxpython==4.0.7
py -3 -m pip install selenium Gooey pynput

(New-Object System.Net.WebClient).DownloadFile('https://chromedriver.storage.googleapis.com/80.0.3987.106/chromedriver_win32.zip', 'C:\Windows\Temp\chromedriver.zip')
(New-Object System.Net.WebClient).DownloadFile('https://chocolatey.org/api/v2/package/chromium/80.0.3987.149', 'C:\Windows\Temp\chromium.zip')
Expand-Archive -Force C:\Windows\Temp\chromium.zip C:\Windows\Temp\
Copy-Item C:\Windows\Temp\tools\chromium* "C:\Program Files (x86)\AUToloka\"
Expand-Archive -Force C:\Windows\Temp\chromedriver.zip "C:\Program Files (x86)\AUToloka\"
	

