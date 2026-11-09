; NSIS installer for MICHO - Windows 11 Dynamic Island AI Companion
; https://github.com/kayefande-droid/micho-michael

;-- General Installer Settings --
Name "MICHO"
Unicode true
;InstallDir "$PROGRAMFILES64\MICHO"
;RequestExecutionLevel admin

;-- Default Installation Directory --
InstallDir "$APPDATA\MICHO"

;-- Output Setup --
;OutFile "MICHO-Installer.exe"

;-- Installer Icon --
;File /r "MICHO/assets/icons/app-icon.ico"

;-- Days to install --
;DaysValidUntil /i 2027.12.31

;-- Pages --
InstallOptionsPage /GROUP "Setup Type" "Minimum features available"
InstallOptionsPage DirectoryPage
InstallOptionsPage FinishPage

;-- Sections --
Section "DefaultInstall" SecDefault
  ;Create shortcuts
  CreateDirectory "$INSTDIR"
  
  ;Copy application files
  File /r "dist-micho\*"
  
  ;Create uninstaller
  WriteUninstaller
   
  ;Create startup shortcut
  ;SendToProgramsFolder "$PROGRAMS\MICHO"
  
  ;Create desktop shortcut
  ;CreateDesktopShortcut "$DESKTOP\MICHO.lnk" "$INSTDIR\MICHO.exe"
SectionEnd

Section "Uninstall"
  ;Remove application
  Delete "$INSTDIR\*"
  RMDir "$INSTDIR"
  
  ;Remove shortcuts
  ;SendToProgramsFolder Remove
  ;RemoveDesktopShortcut "$DESKTOP\MICHO.lnk"
SectionEnd

;-- Installer Information --
;XML
;Name "MICHO"
;Vendor "kayefande-droid"
;Version 1.0
;Description "Windows 11 Dynamic Island AI Companion - Liquid Glass Design"
;UpdateAvailable /s
