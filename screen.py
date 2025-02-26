import win32api
import win32con

def get_resolution():
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return dm.PelsWidth, dm.PelsHeight

def change_resolution(width, height):
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    dm.PelsWidth = width
    dm.PelsHeight = height
    result = win32api.ChangeDisplaySettings(dm, 0)

def main():
    small_mode = (1920, 1080)
    large_mode = (3840, 2400)
    
    current_width, current_height = get_resolution()
    
    if (current_width, current_height) == large_mode:
        change_resolution(*small_mode)
    else:
        change_resolution(*large_mode)

if __name__ == "__main__":
    main() 
