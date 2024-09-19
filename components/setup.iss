; Inno Setup Script

[Setup]
; Define the name and version of the application
AppName=MyPass
AppVersion=1.0
DefaultDirName={commonpf}\MyPass
DefaultGroupName=MyPass
OutputDir=.\Output
OutputBaseFilename=MyPassInstaller
Compression=lzma
SolidCompression=yes
PrivilegesRequired=admin

[Files]
; Add the application executable
Source: "main.exe"; DestDir: "{app}"; Flags: ignoreversion
; Add the logo image
Source: "logo.png"; DestDir: "{app}"; Flags: ignoreversion
; Add the icon file
Source: "logo.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
; Create a shortcut in the Start Menu
Name: "{group}\MyPass"; Filename: "{app}\main.exe"; IconFilename: "{app}\logo.ico"
; Create a shortcut on the Desktop
Name: "{userdesktop}\MyPass"; Filename: "{app}\main.exe"; IconFilename: "{app}\logo.ico"

[Registry]
; Optional: Add registry entries if needed

[Run]
; Optional: Specify if you want to run the application after installation
Filename: "{app}\main.exe"; Description: "Launch MyPass"; Flags: nowait postinstall skipifsilent
