import tkinter as tk
import time
import math

class MixedClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Mixed Functionality Clock")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, width=400, height=400, bg='white')
        self.canvas.pack()
        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        self.draw_clock()
        self.after(1000, self.update_clock)

    def draw_clock(self):
        # Get current time
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Convert to angles
        hour_angle = (360 / 12) * (hours + minutes / 60) - 90
        minute_angle = (360 / 60) * (minutes + seconds / 60) - 90
        second_angle = (360 / 60) * seconds - 90

        # Draw clock face
        self.canvas.create_oval(20, 20, 380, 380)

        # Draw hour hand
        self.draw_hand(hour_angle, 100, f"{hours:01} ", 20)

        # Draw minute hand
        self.draw_hand(minute_angle, 120, f"{minutes:01} ", 15)

        # Draw second hand
        self.draw_hand(second_angle, 140, f"{seconds:01} ", 10)

    def draw_hand(self, angle, length, text, font_size):
        # Calculate hand end position
        angle_rad = math.radians(angle)
        
        # Define gap between digits
        gap = 6  # Adjust this value for more or less gap

        # Draw the digits along the hand
        num_digits = 5  # Number of digits to draw
        for i in range(num_digits):
            digit_x = 200 + (length / num_digits) * (i + 1.5) * math.cos(angle_rad) + (gap * i * math.cos(angle_rad))
            digit_y = 200 + (length / num_digits) * (i + 1.5) * math.sin(angle_rad) + (gap * i * math.sin(angle_rad))
            self.canvas.create_text(digit_x, digit_y, text=text.strip(), font=("Arial", font_size))

if __name__ == "__main__":
    clock = MixedClock()
    clock.mainloop()
