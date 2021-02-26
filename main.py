import PyAutoGUI, time
time.sleep(5)
f = open("ww2.txt", 'r')
for word in f:
  time.sleep()
  PyAutoGUI.typewrite(word)
  PyAutoGUI.press("enter")
