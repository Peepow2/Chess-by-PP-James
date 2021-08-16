import pyautogui
import time as tm

def AutoClick(x, y, clicks, delay, tt):
    tm.sleep(3)
    t2 = t1 = tm.time();
    while(t2 - t1 <= tt):
        pyautogui.moveTo(x, y)
        pyautogui.click(clicks=clicks)
        tm.sleep(delay)
        t2 = tm.time()
    print("Finish");
        
# Driver Code
tt = int(input("ให้กดเองกี่วินาที: " ))
AutoClick(1000, 540, 11, 0.25, tt)
