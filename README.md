# Pid controller with resistor heating using STM32 microcontroller
## End of semester project for Microprocessor Systems
> Measurement and regulation of the temperature of the 39 ohm ceramic resistor using BMP280 sensor

## Completed project assumptions: 
  * error < 1% 
  * setting the desired temperature using serial port
  * displaying current temperature using serial port
  * dedicated script for logging error, desired and measured signal 
  * visualization in Python


## General Information
The main goal of this project is to identify the object in open loop, create a theoretical model, simulate a circuit in Simulink,
create a two-position controller and implement it using physical object. Then create a theoretical PID simulation in Simulink with 
specific kp, ki, kd gains and implement the same circuit using physical object.


## Technologies Used
- STM32 F7 series Microcontroller
- C language for hardware-side implementation
- Python for connecting via serial port with microcontroller, logging and displaying measurements
- Matlab with Simulink for plotting, creating theoretical model, selecting optimal PID parameters

## Video
[Working example](https://youtu.be/75X0-YC5bIA)


## Screenshots
![image](https://user-images.githubusercontent.com/74473601/214701602-ebe40de0-f3c5-4e6e-a957-33e021a9862c.png)
![pid_real_object](https://user-images.githubusercontent.com/74473601/214701912-200e0122-3b2f-41fc-8925-e5bfdd5a0aeb.png)
<img width="805" alt="real_scheme" src="https://user-images.githubusercontent.com/74473601/214702393-692c6d41-d21b-4a08-9634-9a37b8e89701.png">


## Project Status
Project is: _complete_ 


## Room for Improvement
Room for improvement:
- Fine-tune PID parameters for optimal control
