import tkinter as tk


class CountVisitors:
    """
    GUI Application which counts how many visitors enter the building.
    The application prints the count of visitors in the console
    """
    def __init__(self, master):
        self.master = master

        self.button1 = tk.Button(self.master, text="Count", command=self.count_visitors)
        self.button2 = tk.Button(self.master, text="Exit", command=self.close_window)

        self.button1.pack(side=tk.LEFT)
        self.button2.pack(side=tk.LEFT)

        self.button_clicks = 0

    def count_visitors(self):
        self.button_clicks += 1
        print(self.button_clicks)

    def close_window(self):
        self.master.destroy()


def main():
    root = tk.Tk()
    CountVisitors(root)
    root.mainloop()

if __name__ == '__main__':
    main()
