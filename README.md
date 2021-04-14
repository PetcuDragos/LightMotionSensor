# solo-project-PetqDrekoj
solo-project-PetqDrekoj created by GitHub Classroom


# Overview

 I will build a device that has a red LED that lights up when it's dark and feels movement. I will need a motion sensor, light sensor and a LED.

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



![alt text](https://github.com/at-cs-ubbcluj-ro/solo-project-PetqDrekoj/blob/master/presentation.gif)

Here I have a link of a YouTube presentation 
https://www.youtube.com/watch?v=U8aAcIitLM0
