
Analog Clock Using Python
import tkinter as Tkinter
import math
import time

class Clock(Tkinter.Tk):
    def __init__(self):
        super().__init__()
        self.x = 150  # Center Point x
        self.y = 150  # Center Point y
        self.length = 50  # Stick Length
        self.title("Clock")
        self.geometry("300x300")
        self.create_canvas()
        self.create_background()
        self.create_sticks()
        self.update_clock()

    def create_canvas(self):
        self.canvas = Tkinter.Canvas(self, bg='black')
        self.canvas.pack(expand='yes', fill='both')

    def create_background(self):
        try:
            self.image = Tkinter.PhotoImage(file='Clock.gif')
            self.canvas.create_image(150, 150, image=self.image)
        except Tkinter.TclError:
            print("Background image file not found.")

    def create_sticks(self):
        self.sticks = []
        for i in range(3):
            stick = self.canvas.create_line(self.x, self.y, self.x + self.length, self.y + self.length, width=2, fill='red')
            self.sticks.append(stick)

    def update_clock(self):
        now = time.localtime()
        hour = now.tm_hour % 12  # Convert 24-hour format to 12-hour format
        minutes = now.tm_min
        seconds = now.tm_sec

        angles = [(hour * 30 + minutes / 2, minutes * 6, seconds * 6)]  # Convert to degrees
        for n, angle in enumerate(angles[0]):
            x1, y1 = self.x, self.y
            x2 = self.x + self.length * math.cos(math.radians(angle - 90))
            y2 = self.y + self.length * math.sin(math.radians(angle - 90))
            self.canvas.coords(self.sticks[n], x1, y1, x2, y2)

        self.after(1000, self.update_clock)  # Update every second

if __name__ == '__main__':
    app = Clock()
    app.mainloop()
