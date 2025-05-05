import win32api
import win32con
import sys

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
    
    # 检查命令行参数
    if len(sys.argv) > 1:
        arg = sys.argv[1].lower()
        if 'b' in arg:
            change_resolution(*large_mode)
            return
        elif 's' in arg:
            change_resolution(*small_mode)
            return
    
    # 无参数或参数不匹配时，自动切换到另一种模式
    current_width, current_height = get_resolution()
    
    if (current_width, current_height) == large_mode:
        change_resolution(*small_mode)
    else:
        change_resolution(*large_mode)

if __name__ == "__main__":
    main() 
