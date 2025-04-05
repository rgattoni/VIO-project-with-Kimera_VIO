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
The first step to do is to collect data using respectively "Crazyradio" and Wifi of AI_deck. So connect via USB the "Crazyradio" to the PC and then turn on "Crazyflie". Now You should open a terminal and execute `$ cfclient`, insert the correct address, click connect and then select "save" and "write to file" the correct configuratiuon inside "Log block". In parallel with this, open another terminal and execute inside a virtual environment the following commands

     `$ cd aideck-gap8-examples/examples/other/wifi-img-streamer`
     
     `$ python3 opencv-viewer.py --save /path_dove_salvare_le immagini`

Now It is possible to get back the file.csv inside this path `~/.config/cfclient/logdata/datetime_del_file` and the file containing the images of the monocamera in `/aideck-gap8-examples/examples/other/stream_out`. 

     

# Contributions
specify each member's contributions

# Credits
what we used to realize the project like papers or what else
