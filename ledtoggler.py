from tkinter import*
import tkinter.font
from gpiozero import LED
import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)


win = Tk()
win.title("LED Toggler");
Font = tkinter.font.Font(family='Aerial', size = 16, weight = "bold")

value = IntVar()
red_led = LED(14)
green_led = LED(15)
red2_led = LED(18) 


def ledtoggle():
    value1 = value.get()
    if value1 == 1:
        red_led.on()
        green_led.off()
        red2_led.off()
    elif value1 == 2:
        red_led.off()
        green_led.on()
        red2_led.off()
    elif value1 == 3:
        red_led.off()
        green_led.off()
        red2_led.on()
    else :
        red_led.off()
        green_led.off()
        red2_led.off()
        
def close():
    win.destroy()
    GPIO.cleanup()
    
    
ledbutton1 = Radiobutton(win, text = "turn the first red led on", font = Font, variable = value, value = 1, command = ledtoggle, bg = 'bisque2', height = 1, width = 24)
ledbutton1.grid(row = 0, column = 1)

ledbutton2 = Radiobutton(win, text = "turn the green led on", font = Font, variable = value, value = 2, command = ledtoggle, bg = 'bisque2', height = 1, width = 24)
ledbutton2.grid(row = 1, column = 1)

ledbutton3 = Radiobutton(win, text = "turn the second red led on", font = Font, variable = value, value = 3, command = ledtoggle, bg = 'bisque2', height = 1, width = 24)
ledbutton3.grid(row = 2, column = 1)

closebutton = Radiobutton(win, text = "EXIT GUI", font = Font,command = close, bg = 'bisque2', height = 1, width = 24)
closebutton.grid(row = 3, column = 1)



