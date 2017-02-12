

from frames.mainframe import MainFrame
from tkinter import Tk

import os

#==================================================

if __name__ == "__main__":

    print("Hello :D !")
    root = Tk()

    root.title("Writer alpha")
    # try:
    #     # currentdir = os.path.dirname(os.path.abspath(__file__))
    #     # ipath = os.path.join(currentdir, "betterave.xbm")
    #     # root.iconbitmap("@" + ipath)
    # except Exception as e:
    #     print(e)

    f = MainFrame(root)
    root.mainloop()
    print("Goodbye ;) !")

