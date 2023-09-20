# http://www.kbdedit.com/manual/low_level_vk_list.html

import time as t 
import win32gui, win32ui, win32con

Helloworld = '''Hello World.
Please wait a few seconds
. . .

'''

game = True
loops = 0

def main(loops):
    while loops >= 0:
        t.time()
        window_name = 'Leaf Blower Revolution'
        hwnd = win32gui.FindWindow(None, window_name)
        win = win32ui.CreateWindowFromHandle(hwnd)
    
        win.SendMessage(win32con.WM_KEYDOWN, 0x27, 0)
        t.sleep(5)
        win.SendMessage(win32con.WM_KEYUP, 0x27, 0)
    
        win.SendMessage(win32con.WM_KEYDOWN,0x28 ,0)
        t.sleep(0.1)
    
        win.SendMessage(win32con.WM_KEYUP,0x28, 0)
        win.SendMessage(win32con.WM_KEYDOWN, 0x25, 0)
        t.sleep(5)
        win.SendMessage(win32con.WM_KEYUP, 0x25, 0)
    
        win.SendMessage(win32con.WM_KEYDOWN, 0x26, 0)
        t.sleep(0.1)
        win.SendMessage(win32con. WM_KEYUP, 0x26, 0)
    
        passed = t.ctime()
        
        loops = loops + 1
        print(f'loop {loops} finished at {passed}')


while game == True:
    try:
        print(Helloworld)
        main(loops)
        
    except win32ui.error:
        print('-Please start the game first-')
        break
