# Tingo
> AdaFruit NeoPixel controller for Raspberry Pi with MQTT

## Prerequisites
- A Raspberry Pi (Any model with internet connectivity)
- The [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library by Jeremy Garff
- [NeoPixel](https://learn.adafruit.com/adafruit-neopixel-uberguide/overview) compatible LEDs
- An MQTT Broker (I would suggest [Mosquitto](https://mosquitto.org))

## Setup
- Download and install the [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library
- Download Tingo
  - Clone this repo: `git clone https://github.com/RajatJacob/tingo.git`
  - or [dowload the source code](https://github.com/RajatJacob/tingo/releases) of the latest release (.ZIP) or (.TAR.GZ).

```
cd tingo/
python setup.py
```
- Enter the details of your MQTT broker.
  - IP Address/Hostname
  - Port
  - Username
  - Password

- Enter the details of the client
  - Client ID
  - Device type (ws281x)
  - GPIO pin to contol

- (Optional)
  - Create a global symlink of the bash script.
```
cd tingo/
sudo ln tingo /usr/bin/tingo
```

## Usage
```tingo {start|stop|restart|update}```

- ```tingo start```
  - Start Tingo. (or create a new instance of Tingo - Not recommended)
- ```tingo stop```
  - Stop all running instances of Tingo.
- ```tingo restart```
  - Restart Tingo all stop all extra running instances.
- ```tingo update```
  - Get updates from GitHub and restart Tingo.
