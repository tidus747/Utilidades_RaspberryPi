import RPi_I2C_driver as I2C_LCD_driver
from time import *

mylcd = I2C_LCD_driver.lcd()

fontdata1 = [
        # char(0) - Upper-left character
        [ 0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b11111,
          0b11111 ],

        # char(1) - Upper-middle character
        [ 0b00000,
          0b00000,
          0b00100,
          0b00110,
          0b00111,
          0b00111,
          0b11111,
          0b11111 ],

        # char(2) - Upper-right character
        [ 0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b10000,
          0b11000 ],

        # char(3) - Lower-left character
        [ 0b11111,
          0b11111,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000 ],

        # char(4) - Lower-middle character
        [ 0b11111,
          0b11111,
          0b00111,
          0b00111,
          0b00110,
          0b00100,
          0b00000,
          0b00000 ],

        # char(5) - Lower-right character
        [ 0b11000,
          0b10000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000,
          0b00000 ],
]

mylcd.lcd_load_custom_chars(fontdata1)

mylcd.lcd_write(0x80)
mylcd.lcd_write_char(0)
mylcd.lcd_write_char(1)
mylcd.lcd_write_char(2)

mylcd.lcd_write(0xC0)
mylcd.lcd_write_char(3)
mylcd.lcd_write_char(4)
mylcd.lcd_write_char(5)
