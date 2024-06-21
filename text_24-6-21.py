import psutil
import win32gui
import win32process
import time
import pyautogui

import pygetwindow
import win32api
import win32con

import ttkbootstrap as ttk
import tkinter as tk
from ttkbootstrap import Style
from ttkbootstrap.constants import *


class Application():
    def __init__(self, root):
        self.root = root

        self.style = Style(theme='litera')
        self.root.title('黄泉全自动差分宇宙')
        self.root.geometry(f"400x150")
        self.root.minsize(400, 150)
        self.root.resizable(False, False)
        self.create_widgets()

        #差分初始化
        self.exe_name = "StarRail.exe"
        self.pid = self.find_process_by_name(self.exe_name)
        if not self.pid:
            print(f"未找到运行中的应用程序: {self.exe_name}")
            exit()
        else:
            print(f"找到应用程序 {self.exe_name} 的PID: {self.pid}")

        self.hwnd = self.find_window_by_pid(self.pid)

        if not self.hwnd:
            print(f"未找到PID为 {self.pid} 的窗口")
            exit()
        else:
            print(f"成功获取到窗口句柄: {self.hwnd}")

        win32gui.SetForegroundWindow(self.hwnd)

    def create_widgets(self):
        self.main_frame = ttk.Frame(self.root)
        self.main_frame.pack(side=tk.RIGHT, pady=20, fill=BOTH, expand=True)

        #标签提醒
        self.label_description = ttk.Label(self.main_frame, text='1080p窗口 打开差分宇宙 点启动')
        self.label_description.pack(side=tk.TOP,pady=10)

        # 开始按钮&结束按钮
        self.btn_start = ttk.Button(self.main_frame, text="启动",command= self.routine)
        self.btn_start.pack(side=tk.TOP,pady=10)


# class Auto_hq_chafen:
#     def __init__(self):

    def find_process_by_name(self, exe_name):
        for proc in psutil.process_iter(['pid', 'name']):
            if proc.info['name'] == exe_name:
                return proc.info['pid']
        return None


    def find_window_by_pid(self,pid):
        def enum_window_titles(hwnd, result):
            if win32gui.IsWindowVisible(hwnd):
                _, found_pid = win32process.GetWindowThreadProcessId(hwnd)
                if found_pid == pid:
                    result.append(hwnd)
        windows = []
        win32gui.EnumWindows(enum_window_titles, windows)
        return windows[0] if windows else None

#设置副屏
# left, top = (-1920,1080) #副屏全屏
# zoomscale1 = 1.75
# zoomscale2 = 1.25

#pyautogui.FAILSAFE = False

    def Click1(self,x,y):
        left, top, right, bottom = win32gui.GetWindowRect(self.hwnd) #主屏窗口
        w_left = left+12
        w_top = top+52

        # ABSPosition = [(left+x)*zoomscale1/zoomscale2, (top+y)*zoomscale1/zoomscale2] #在副屏上
        ABSPosition = [(w_left + x) , (w_top + y) ] #在主屏上 窗口坐标差(-12,-52)

        pyautogui.moveTo(ABSPosition[0], ABSPosition[1], duration=0.05)
        #pyautogui.click(clicks = 2, interval = 0.05)
        pyautogui.click()
        print(f"点击了({ABSPosition })")


    def shaguai(self):
        print(f"清怪开始")
        pyautogui.press('4')
        time.sleep(0.2)
        pyautogui.keyDown('w')
        for i in range(16):
            pyautogui.press('e')
            time.sleep(0.3)
        pyautogui.keyUp('w')
        time.sleep(0.1)
        pyautogui.press('w')
        print(f"清怪结束")



#for i in range(1):
#while True:
    def routine(self):
        time.sleep(0.2)
        #开始游戏
        self.Click1( 1600, 950)
        time.sleep(2)
        #常规演算
        self.Click1( 380, 360)
        time.sleep(2)
        #启动
        self.Click1( 1700, 960)
        time.sleep(8.5)


        #方程3
        self.Click1( 1400, 400)
        time.sleep(2)
        #确认
        self.Click1( 1700, 960)
        time.sleep(3)

        #祝福3
        self.Click1( 1400, 400)
        time.sleep(2)
        #确认
        self.Click1( 1700, 960)
        time.sleep(3)

        #点击空白
        self.Click1( 1700, 960)
        time.sleep(1.5)

        #点击空白
        self.Click1( 1700, 960)
        time.sleep(3)

        #EE 杀怪
        self.shaguai()
        time.sleep(3)

        #4次祝福
        for i in range(4):
            self.Click1( 1400, 400)
            time.sleep(2)
            self.Click1( 1700, 960) #确认
            time.sleep(3)

        #ESC 退出
        pyautogui.press('esc')
        time.sleep(2)

        #结算退出
        self.Click1( 1700, 960)
        time.sleep(1)

        #确认
        self.Click1( 1200, 770)
        time.sleep(8.5)

        #返回主界面
        self.Click1( 955, 955)
        time.sleep(4)

if __name__ == '__main__':
    root = ttk.Window()
    app = Application(root)
    root.mainloop()