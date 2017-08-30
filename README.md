# White Rabbit

Neopixel based XY Matrix running via Raspberry Pi to display time, weather, and news.

![White Rabbit](https://github.com/jwalanta/whiterabbit/raw/master/whiterabbit.jpg)

## Requirements

### Hardware
- Raspberry Pi
- Neopixel strips (144 leds/m recommended). Get it from either [Adafruit](https://www.adafruit.com/product/1506) or much cheaper options at AliExpress (search for "ws2812b led strips")

### Software
- Any Linux based OS running on Raspberry Pi
- Python
- [rpi_ws281x library](https://github.com/jgarff/rpi_ws281x). Tutorial on using: https://learn.adafruit.com/neopixels-on-raspberry-pi/overview

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

### Displaying 

## Weather data

Weather data is from [Wunderground](https://www.wunderground.com/weather/api/d/docs). They have a pretty nice api for current weather conditions and daily forecast. The free plan is good for 500 calls per day and 10 calls per minute. To make a call every 15 minutes, it's sufficient.

The data is retrieved and stored to a file on disk via cron job.

## Cron jobs

Cron jobs look something like this (replace <key> with api key, state and city appropriately)
```
# weather data, every 15 minutes
*/15 * * * * curl 'http://api.wunderground.com/api/<key>/conditions/q/CA/San_Francisco.json' > /var/cache/conditions.json
*/15 * * * * curl 'http://api.wunderground.com/api/<key>/forecast/q/CA/San_Francisco.json' > /var/cache/forecast.json
```

## What's in the name?

It's **Neo**pixel **Matrix**, so it's got to have some reference to the movie.

https://www.youtube.com/watch?v=6IDT3MpSCKI

