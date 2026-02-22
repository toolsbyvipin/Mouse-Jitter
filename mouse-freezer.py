def freeze_mouse():
    """Alternative: Rapid micro-movements to simulate freeze"""
    screen_width, screen_height = pyautogui.size()
    x, y = pyautogui.position()
    
    for _ in range(1000):  # 1000 rapid micro-movements
        pyautogui.moveTo(x + random.randint(-1, 1), y + random.randint(-1, 1), duration=0)
