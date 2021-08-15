import pyautogui
import time as tm

def AutoClick(x, y, clicks, delay, tt):
    t1 = tm.time();
    t2 = -1
    tm.sleep(3)
    while(t2-t1 <= tt):
        pyautogui.moveTo(x, y)
        pyautogui.click(clicks=clicks)
        tm.sleep(delay)
        t2 = tm.time()
    print("Finish");
        
# Driver Code
tt = int(input("ให้กดเองกี่วินาที: " ))
AutoClick(450, 530, 12, 0.4, tt)
