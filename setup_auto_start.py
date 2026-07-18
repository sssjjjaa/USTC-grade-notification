import os
import sys
import winshell
from win32com.client import Dispatch


def setup_auto_start(enable=True):
    startup_folder = winshell.startup()
    script_path = os.path.abspath(os.path.join(os.path.dirname(__file__), 'run.bat'))
    shortcut_name = 'USTC成绩监控.lnk'
    shortcut_path = os.path.join(startup_folder, shortcut_name)

    if enable:
        if not os.path.exists(script_path):
            print(f"错误：未找到脚本文件 {script_path}")
            return False

        shell = Dispatch('WScript.Shell')
        shortcut = shell.CreateShortCut(shortcut_path)
        shortcut.TargetPath = script_path
        shortcut.WorkingDirectory = os.path.dirname(script_path)
        shortcut.save()

        print(f"已设置开机自启动，快捷方式已创建：{shortcut_path}")
        return True
    else:
        if os.path.exists(shortcut_path):
            os.remove(shortcut_path)
            print(f"已取消开机自启动，快捷方式已删除：{shortcut_path}")
            return True
        else:
            print("未找到开机自启动快捷方式")
            return False


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1].lower() == 'disable':
        setup_auto_start(False)
    else:
        setup_auto_start(True)