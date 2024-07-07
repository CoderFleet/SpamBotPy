import time
import pyautogui as pyg

print("Press 1 for Default Spam\nPress 2 for Bee Spam")

in = input("-->")

if (in == 1) :
    print("It's Gonna Start Now... Move your text cursor focus to the")
    print("Required Text Field")

    time.sleep(30)

    for i in range(100):
        pyg.press("Y")
        pyg.press("u")
        pyg.press("o")
        pyg.press("enter")
        pyg.press("a")
        pyg.press("r")
        pyg.press("e")
        pyg.press("enter")
        pyg.press("s")
        pyg.press("p")
        pyg.press("a")
        pyg.press("m")
        pyg.press("m")
        pyg.press("e")
        pyg.press("d")
        pyg.press("enter")
        pyg.press("b")
        pyg.press("y")
        pyg.press("enter")
        pyg.press("R")
        pyg.press("P")
        pyg.press("S")

elif (in == 2):
    print("It's Gonna Start Now... Move your text cursor focus to the")
    print("Required Text Field")
    time.sleep(30)f = open("bee.txt", "r")
    for word in f:
        pyautogui.typewrite(word)
        pyautogui.press("enter")






