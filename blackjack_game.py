from deck import Deck
from hand import Hand
from utils import *
from gui import *

def main():
    root = tk.Tk()
    gui = BlackjackGUI(root)
    root.mainloop()


if __name__ == "__main__":
    main()