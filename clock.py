import tkinter as tk
import time
import math

class DigilogClock(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Digilog Clock")
        self.geometry("400x400")
        self.canvas = tk.Canvas(self, width=400, height=400, bg='lightblue')  
        self.canvas.pack()
        self.update_clock()

    def update_clock(self):
        self.canvas.delete("all")
        self.draw_clock()
        self.after(1000, self.update_clock)

    def draw_clock(self):
        current_time = time.localtime()
        hours = current_time.tm_hour % 12
        minutes = current_time.tm_min
        seconds = current_time.tm_sec

        # Conversion to angles
        hour_angle = (360 / 12) * (hours + minutes / 60) - 90
        minute_angle = (360 / 60) * (minutes + seconds / 60) - 90
        second_angle = (360 / 60) * seconds - 90

        # Clock face
        self.canvas.create_oval(20, 20, 380, 380)  
        self.canvas.create_oval(25, 25, 375, 375, outline='black', width=2) 

        # Hands in layering order
        self.draw_hand(second_angle, 125, f"{seconds:01} ", 10, fill='red')  
        self.draw_hand(minute_angle, 115, f"{minutes:01} ", 15)  
        self.draw_hand(hour_angle, 90, f"{hours:01} ", 20)  

        # Hour Marks
        for i in range(12): 
            angle = math.radians(i * 30 - 90)           # 30 degrees for each hour
            x_start = 200 + 130 * math.cos(angle)       # Start point (inner circle)
            y_start = 200 + 130 * math.sin(angle)
            x_end = 200 + 150 * math.cos(angle)         # End point (outer circle)
            y_end = 200 + 150 * math.sin(angle)
            self.canvas.create_line(x_start, y_start, x_end, y_end, fill='black', width=2)

        # # Minute tick marks
        # for i in range(60):  
        #     angle = math.radians(i * 6 - 90)          # 6 degrees for each minute
        #     x_start = 200 + 140 * math.cos(angle)     # Start point (inner circle)
        #     y_start = 200 + 140 * math.sin(angle)
        #     x_end = 200 + 150 * math.cos(angle)       # End point (outer circle)
        #     y_end = 200 + 150 * math.sin(angle)
        #     self.canvas.create_line(x_start, y_start, x_end, y_end, fill='black', width=1)



    def draw_hand(self, angle, length, text, font_size, fill='black'):
        # Hand's end position
        angle_rad = math.radians(angle)
        
        gap = 6  

        num_digits = 5  
        for i in range(num_digits):
            digit_x = 200 + (length / num_digits) * (i + 1.5) * math.cos(angle_rad) + (gap * i * math.cos(angle_rad))
            digit_y = 200 + (length / num_digits) * (i + 1.5) * math.sin(angle_rad) + (gap * i * math.sin(angle_rad))
            self.canvas.create_text(digit_x, digit_y, text=text.strip(), font=("Arial", font_size), fill=fill)

if __name__ == "__main__":
    clock = DigilogClock()
    clock.mainloop()
