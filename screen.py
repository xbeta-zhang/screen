import win32api
import win32con

def get_current_resolution():
    """获取当前屏幕分辨率"""
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    return dm.PelsWidth, dm.PelsHeight

def change_resolution(width, height):
    """更改屏幕分辨率"""
    dm = win32api.EnumDisplaySettings(None, win32con.ENUM_CURRENT_SETTINGS)
    dm.PelsWidth = width
    dm.PelsHeight = height
    
    # 尝试更改分辨率
    result = win32api.ChangeDisplaySettings(dm, 0)
    
    if result == win32con.DISP_CHANGE_SUCCESSFUL:
        print(f"成功将分辨率更改为 {width}x{height}")
    else:
        print("更改分辨率失败")

def main():
    # 定义两种分辨率模式
    small_mode = (1920, 1080)
    large_mode = (3840, 2400)
    
    # 获取当前分辨率
    current_width, current_height = get_current_resolution()
    print(f"当前分辨率：{current_width}x{current_height}")
    
    # 根据当前分辨率切换到另一种模式
    if (current_width, current_height) == large_mode:
        change_resolution(*small_mode)
    else:
        # 如果不是大屏模式，则切换到大屏模式
        change_resolution(*large_mode)

if __name__ == "__main__":
    main() 