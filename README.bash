#Install requirements:
python -m venv venv
source venv/bin/activate
pip install pyautogui pyinstaller

pyinstaller --onefile --noconsole --name "SystemUpdate.exe" mouse_jitter.py

jitter_duration = 60  # Increase to 1 minute
jitter_intensity = 25  # More aggressive movement
