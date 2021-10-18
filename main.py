# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import time


def print_hi(name,x):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name},第 {x} 次')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = 0
    while x < 10:
        x = x + 1
        print_hi('PyCharm',x)
        time.sleep(1)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
