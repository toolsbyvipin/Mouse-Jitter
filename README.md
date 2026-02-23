#No file needed

CHECK One-Liner-Jitter 
One-Liner-Freezer



#Install requirements:
python -m venv venv
source venv/bin/activate
pip install pyautogui pyinstaller

pyinstaller --onefile --noconsole --name "SystemUpdate.exe" mouse_jitter.py


