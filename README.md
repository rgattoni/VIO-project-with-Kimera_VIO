# VIO-project-with-Kimera_VIO
Implement a VIO algorithm for Crazyflie

# Installation Requirements
Lists of software and hardaware to execute the application:
Tested on Ubuntu 24.04 LTS.
## Prerequisites:
* cflib
* cfclient
The necessary "Crazyflie" software is installed within a virtual environment to avoid conflicts with the system's Python and pip. Following commands to execute a virtual env inside the project file:

     `$ python3 -m venv cfclient-env`

     `$ source cfclient-env/bin/activate`
 
     `$ pip3 install cfclient`
 
     `$ pip3 install cflib`

It is also necessary to install the driver for "Crazyradio 2.0" and here are the instructions [https://www.bitcraze.io/documentation/repository/crazyradio-firmware/master/building/usbwindows/](URL)
Crazyradio allows data communication between the drone and the client by running `$ cfclient` from the terminal. Then It's possible to see the output in the relative path `~/.config/cfclient/logdata/datetime_del_file`. This output file can be saved by setting the relevant "Logging configuration" within cfclient and then inserting it into the "Log block". 



# Repository Structure
provide an overview of project's folder and file organization

# Demo Instructions
include all commands to reproduce the demo

# Contributions
specify each member's contributions

# Credits
what we used to realize the project like papers or what else
