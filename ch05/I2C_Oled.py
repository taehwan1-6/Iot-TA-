import time
import Adafruit_SSD1306
from PIL import Image, ImageDraw, ImageFont
import Adafruit_BMP.BMP085 as BMP085

disp = Adafruit_SSD1306.SSD1306_128_64(rst=None, i2c_address=0x3C)

disp.begin()

disp.clear()
disp.display()

width = disp.width
height = disp.height
image = Image.new('1', (width, height))

draw = ImageDraw.Draw(image)

draw.rectangle((0,0,width,height), outline=0, fill=0)

padding = -2
top = padding
bottom = height-padding

x = 0

font = ImageFont.load_default()

sensor = BMP085.BMP085()

while True:
    temp = sensor.read_temperature()
    pressure = sensor.read_pressure()
    altitude = sensor.read_altitude()
    
    print('Temp = {0:0.2f} *C'.format(temp))
    print('Pressure = {0:0.2f} Pa'.format(pressure))
    print('Altitude = {0:0.2f} m'.format(altitude))
    
    draw.text((x,top),'Temp = {0:0.2f} *C'.format(temp), font=font, fill=255)
    draw.text((x,top+8),'Pressure = {0:0.2f} Pa'.format(pressure), font=font, fill=255)
    draw.text((x,top+16),'Altitude = {0:0.2f} m'.format(altitude), font=font, fill=255)
    
    disp.image(image)
    disp.display()
    
    time.sleep(2)
