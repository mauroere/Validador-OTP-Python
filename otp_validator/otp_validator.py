import tkinter as tk
import gui

def main():
    root = tk.Tk()
    app_gui = gui.OTPValidatorGUI(root)
    root.mainloop()

if __name__ == "__main__":
    main()