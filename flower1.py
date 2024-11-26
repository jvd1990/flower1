from turtle import *

def flower():
    speed(0)
    for i in range(300):
        circle(190 - i, 90)  # Draw a partial circle with decreasing radius
        left(90)  # Rotate 90 degrees
        circle(190 - i, 90)  # Draw another partial circle
        left(18)  # Rotate 18 degrees for the overall pattern
flower()
done()
