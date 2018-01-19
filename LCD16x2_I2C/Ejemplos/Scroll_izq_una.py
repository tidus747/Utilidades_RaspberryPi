import RPi_I2C_driver as I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

padding = " " * 16
my_long_string = "This is a string that needs to scroll"
padded_string = my_long_string + padding

for i in range (0, len(my_long_string)):
 lcd_text = padded_string[((len(my_long_string)-1)-i):-i]
 mylcd.lcd_display_string(lcd_text,1)
 sleep(0.4)
 mylcd.lcd_display_string(padding[(15+i):i], 1)
