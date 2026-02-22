import pyautogui
import time
import threading
import random
import sys
import os
from ctypes import windll

# Disable PyAutoGUI failsafe (for testing only)
pyautogui.FAILSAFE = False

def jitter_mouse():
    """Main mouse jitter function"""
    # Get screen dimensions
    screen_width, screen_height = pyautogui.size()
    
    jitter_duration = 30  # seconds of jittering
    jitter_intensity = 15  # pixels to move
    
    start_time = time.time()
    
    while time.time() - start_time < jitter_duration:
        # Generate random small movements
        dx = random.randint(-jitter_intensity, jitter_intensity)
        dy = random.randint(-jitter_intensity, jitter_intensity)
        
        # Get current position
        x, y = pyautogui.position()
        
        # Ensure we don't go off screen
        new_x = max(0, min(screen_width - 1, x + dx))
        new_y = max(0, min(screen_height - 1, y + dy))
        
        # Move mouse
        pyautogui.moveTo(new_x, new_y, duration=0.01)
        
        # Small delay to prevent overwhelming CPU
        time.sleep(0.02)
    
    print("Jitter complete. Exiting...")
    sys.exit(0)

def hide_console():
    """Hide console window for stealth"""
    if os.name == 'nt':  # Windows
        windll.user32.ShowWindow(windll.kernel32.GetConsoleWindow(), 0)

def main():
    # Hide console immediately
    hide_console()
    
    # Small delay to let window hide
    time.sleep(0.1)
    
    # Start jitter in separate thread to avoid blocking
    jitter_thread = threading.Thread(target=jitter_mouse)
    jitter_thread.daemon = True
    jitter_thread.start()
    
    # Keep main thread alive
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        sys.exit(0)

if __name__ == "__main__":
    main()
