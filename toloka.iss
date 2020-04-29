; Script generated by the Inno Setup Script Wizard.
; SEE THE DOCUMENTATION FOR DETAILS ON CREATING INNO SETUP SCRIPT FILES!

#define TolokaName "AUToloka"
#define TolokaVersion "1.0"
#define TolokaPublisher "AUToloka"
#define TolokaURL "https://vk.com/autoloka"

[Setup]
; NOTE: The value of AppId uniquely identifies this application. Do not use the same AppId value in installers for other applications.
; (To generate a new GUID, click Tools | Generate GUID inside the IDE.)
AppId={{CF6FC5C1-7B55-498D-A312-C1DEB5B93AC5}
AppName={#TolokaName}
AppVersion={#TolokaVersion}
;AppVerName={#TolokaName} {#TolokaVersion}
AppPublisher={#TolokaPublisher}
AppPublisherURL={#TolokaURL}
AppSupportURL={#TolokaURL}
AppUpdatesURL={#TolokaURL}
DefaultDirName={autopf}\{#TolokaName}
DefaultGroupName={#TolokaName}
DisableProgramGroupPage=yes
OutputBaseFilename="AUTOLOKA_setup"
; Uncomment the following line to run in non administrative install mode (install for current user only.)
PrivilegesRequired=admin
;PrivilegesRequiredOverridesAllowed=dialog
Compression=lzma
SolidCompression=yes
WizardStyle=modern
LicenseFile="C:\Users\VirtualWin\Desktop\toloka\licence.txt"

[Languages]
Name: "russian"; MessagesFile: "compiler:Languages\Russian.isl"

[Files]
Source: "C:\Users\VirtualWin\Desktop\toloka\toloka.cmd"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs

Source: "C:\Users\VirtualWin\Desktop\toloka\*"; DestDir: "{app}"; Flags: ignoreversion recursesubdirs createallsubdirs; 
; NOTE: Don't use "Flags: ignoreversion" on any shared system files

[Run]
Filename: "{app}\post-install.exe";Description: "Óñòàíîâêà çàâèñèìîñòåé"; Flags: postinstall nowait skipifsilent runascurrentuser
