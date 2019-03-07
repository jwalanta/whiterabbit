# White Rabbit

[Neopixel](https://www.adafruit.com/category/168) based XY Matrix running via Raspberry Pi to display time, weather, and news.

![White Rabbit](https://github.com/jwalanta/whiterabbit/raw/master/whiterabbit.jpg)

## Requirements

### Hardware
- Raspberry Pi
- Neopixel strips (144 leds/m recommended). Get it from either [Adafruit](https://www.adafruit.com/product/1506) or much cheaper options at AliExpress (search for "ws2812b led strips")

### Software
- Any Linux based OS running on Raspberry Pi
- Python
- [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x). Tutorial on using: https://learn.adafruit.com/neopixels-on-raspberry-pi/overview

```
# TL;DR for installing rpi_ws281x library

# install pip if not installed
$ sudo apt install python3-pip

# install libraries
$ sudo pip3 install rpi_ws281x adafruit-circuitpython-neopixel
```

## Running

```
./run.sh
``` 

However, before doing that read how to build the matrix, connect it to Raspberry Pi, and adjust the settings below.

## Building the display matrix

### Neomatrix layout

The leds are arranged this "serpentine" way:

```
  x - x - x - x - x - x - x --- to raspberry pi
  |
  |
  x - x - x - x - x - x - x 
                          |
                          |
  x - x - x - x - x - x - x 
  |
  |
  x - x - x - x - x - x - x 
                          |
                          |
  x - x - x - x - x - x - x 
```

If five strips of neopixels with 144 pixels/m are arranged in this way, the pixel numberings will be as follows:

```
 143 - x - x - x - x - x -- 0 --- to raspberry pi
  |
  |
 144 - x - x - x - x - x - 287
                            |
                            |
 431 - x - x - x - x - x - 288
  |	
  |
 432 - x - x - x - x - x - 575
                            |
                            |
 719 - x - x - x - x - x - 576

```

### Connecting to Raspberry Pi

The 5V and GND pins from the strip can be connected to any 5V and GND pin of Raspberry Pi. If there are lots of pixels and you are planning to use the full brightness, you need to connect it to external power source with higher amp.

The data pin is connected to any GPIO pin with PWM (18 by default).

See https://learn.adafruit.com/adafruit-neopixel-uberguide for more details about connection and best practices.

### Displaying text

[BDF font](https://en.wikipedia.org/wiki/Glyph_Bitmap_Distribution_Format) files are used to read data for each character. Modify the values in `whiterabbit.py` to specify the font file. The `MatrixBuffer` class is used to construct the buffer before sending the data to the neopixel strip. The `NeopixelWrapper::matrix_to_array()` converts the matrix to serial data. If the strips are arranged in a different way than described above, this function has to be adjusted to change the mapping.

`MatrixBuffer` has helper functions to display character text or character.

By default, the current time and weather condition is displayed.

### Scrolling text

The program also reads fifo file at `/tmp/matrix.fifo`. If any line of text is written to it, e.g., `echo 'Hello, World! This is a scrolling test' > /tmp/matrix.fifo`, the text is scrolled on the display. Once the scroll is done, it goes back to displaying time and weather.

## Weather data

Weather data is from [National Weather Service](https://www.weather.gov/). The forecast and current conditions data for a given lat/lon location can be retrieved in json format (among several others).

The data is retrieved and stored to a file on disk via cron job. Cron jobs look something like this (replace lat and lon data appropriately)
```
# weather data, every hour
0 * * * * curl 'https://forecast.weather.gov/MapClick.php?lat=37.7771&lon=-122.4196&unit=0&lg=english&FcstType=json' > /var/cache/forecast.json
```

## What's in the name?

It's **Neo**pixel **Matrix**, so it's got to have some reference to the movie.

https://www.youtube.com/watch?v=6IDT3MpSCKI

