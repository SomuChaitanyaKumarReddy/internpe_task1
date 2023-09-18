import tkinter as tk
from datetime import datetime

class DigitalClock(tk.Frame):
    def __init__(self, master):
        super().__init__(master)

        self.label = tk.Label(self, font=("Helvetica", 40), text=datetime.now().strftime("%H:%M:%S"))
        self.label.pack()

        self.after(1000, self.update_time)

    def update_time(self):
        self.label.config(text=datetime.now().strftime("%H:%M:%S"))
        self.after(1000, self.update_time)

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Digital Clock")

    clock = DigitalClock(root)
    clock.pack()

    root.mainloop()
