# solo-project-PetqDrekoj
solo-project-PetqDrekoj created by GitHub Classroom


# Overview
For my individual project I have decided to build something that will require motion sensor. So my idea is to build a device that has a red LED that lights up when it's dark and feels movement. But in order to do that I am going to need a motion sensor, a light intensity sensor and an LED. The motion sensor will detect when something is near, and the light intensity detects if outside is day or night, the LED here is a replacement for a light bulb. This system is similar to the one used in the flat area when you get near the entrance, when, in case it's dark, a light will shine so you can see the surroundings.


# Schematics
![alt text](https://github.com/at-cs-ubbcluj-ro/solo-project-PetqDrekoj/blob/master/Schematic.PNG?raw=true)

# Pre-requisites

- Raspberry Pi 3+ 
- Light Intensity Sensor (BH1750)
- Ultrasonic Sensor (HC-SR04)
- 1 breadboard
- 12 jumper wires
- 1 LED (red/yellow/green LED)
- 2 270 ohm resistors
- 1 680 ohm resistor

Optional:
- 1 Ethernet Cable (which is needed for the connection with PC/laptop)
- A computer/laptop (where we will deploy the script)


# Setup and Build Plan

1) We will set up the LED. We will use a BCM port for the current input, and a ground for the output. We will also need a resistor of 270 ohms which will be between the input and the anode of the LED. At the cathode we put the ground that is connected to any port of the ground from Raspberry.

2) We will set up the light intensity sensor. We will need a ground port from the Raspberry, a 3.3 V current from the Raspberry and 2 BCM that have I2C interface. We will connect them and then we can check the connection through the command 'sudo i2cdetect -y -1'. 

3) We will set up the ultrasound sensor. We will also need a ground, a current of 5V, 2 BCM/GPIO pins. We will register the Echo and Trigger from these 2 BCM ports. For the Echo port we need firstly to connect it to a resistor of 270 ohm and then connect it to raspberry pi. 

For these connections to work we may use several jumper wires depending of our setup.

Then we just need to power up the raspberry pi and then connect to it with putty or VNC server and run in terminal 'python program.py'. Some Pins might be interchanged, but they need to be set also in the program.py. 



![alt text](https://github.com/at-cs-ubbcluj-ro/solo-project-PetqDrekoj/blob/master/presentation.gif)

Here I have a link of a YouTube presentation 
https://www.youtube.com/watch?v=U8aAcIitLM0

# Conclusions
After working with these sensors, I have come to the conclusion that the light intensity sensor can be easily tricked with a flashlight during nighttime or something that may cover it up during daytime and it will work unadequately. One solution will be to insert time verification so it lights only at specific hours or time frames. Another problem is that the motion sensor can be tricked, but that may be sorted out with some software geeks. One more thing is that I would like in future to change the LED to a light buld and the raspberry pi to something small because it doesn;t need every aspect of the raspberry pi. 
