# Tingo
	AdaFruit NeoPixel controller for Raspberry Pi with MQTT

## Prerequisites
	- Raspberry Pi (Any model with internet connectivity)
	- rpi_ws281x library by Jeremy Garff
	- NeoPixel compatible LEDs
	- MQTT Broker (I would suggest Mosquitto)

## Setup
	- Download and install the [rpi_ws281x](https://github.com/jgarff/rpi_ws281x) library
	- Download Tingo
	-- Clone this repo: `git clone https://github.com/RajatJacob/tingo.git`
	-- or [download the source code](https://github.com/RajatJacob/tingo/releases) of the latest release (.ZIP) or (.TAR.GZ).

	```
	cd tingo/
	python setup.py

	```
	Enter the details of your MQTT broker.

	- (Optional)
	-- Create a global symlink of the bash script.
		```
		cd tingo/
		sudo ln tingo /usr/bin/tingo
		```

## Usage
	```tingo {start|stop|restart|update}```

	- ```tingo start```
	-- Start Tingo. (or create a new instance of Tingo - Not recommended)
	- ```tingo stop```
	-- Stop all running instances of Tingo.
	- ```tingo restart```
	-- Restart Tingo all stop all extra running instances.
	- ```tingo update```
	-- Get updates from GitHub and restart Tingo.