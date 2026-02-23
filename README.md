# Mouse Jitter
## RUN POWERSHELL AS ADMINSTRATOR ON VICTIM'S PC AND PASTE 
```bash
#Run powershell as adminstration on target's OS and paste this to use jitter 

powershell -ExecutionPolicy Bypass -Command "Add-Type -AssemblyName System.Windows.Forms; while ($true) { $pos=[System.Windows.Forms.Cursor]::Position; $randX=Get-Random -Min -5 -Max 5; $randY=Get-Random -Min -5 -Max 5; [System.Windows.Forms.Cursor]::Position=New-Object System.Drawing.Point(($pos.X+$randX),($pos.Y+$randY)); Start-Sleep -m 10 }"

#To stop just close cmd
```

# Mouse Freezer 
```bash
#Run Powershell as admistration on Victim's computer and paste 

powershell -ExecutionPolicy Bypass -Command "Add-Type -AssemblyName System.Windows.Forms; $frozenPos=[System.Windows.Forms.Cursor]::Position; while ($true) { [System.Windows.Forms.Cursor]::Position=$frozenPos; Start-Sleep -m 1 }"

#To stop click ALT + F4
```

## FOR py files 

#Install requirements:
python -m venv venv
source venv/bin/activate
pyinstaller --onefile --noconsole --name "SystemUpdate.exe" mouse_jitter.py


# DEVELOPER

Commands By Vipin to prank your friends
pip install pyautogui pyinstaller


