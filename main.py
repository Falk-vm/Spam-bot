import pyautogui, time
time.sleep(5)
f = open("ww2.txt", 'r')
for word in f:
  time.sleep()
  pyautogui.typewrite(word)
  pyautogui.press("enter")
