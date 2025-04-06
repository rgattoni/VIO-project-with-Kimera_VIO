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

* Kimera-VIO
Now We report the list of commands to install the algorithm and to have it avaiable to usage:

    `$ git clone git@github.com:MIT-SPARK/Kimera-VIO.git`

    `$ cd Kimera-VIO`

Before execute the following commnand It is necessary to apply more than 6Gb of RAM inside the virtual machine.

    `$ sudo docker build --rm -t kimera_vio -f ./scripts/docker/Dockerfile .`

After that It's possible to run the docker container with the correct set-up of the main algorithm and You can do this with the command:

     `$ sudo ./scripts/docker/kimera_vio_docker.bash`


# Repository Structure
Provide an overview of project's folder and file organization

# Demo Instructions
Include all commands to reproduce the demo
The first step to do is to collect data using respectively "Crazyradio" and Wifi of AI_deck. So connect via USB the "Crazyradio" to the PC and then turn on "Crazyflie". Now You should open a terminal and execute `$ cfclient`, insert the correct address, click connect and then select "save" and "write to file" the correct configuratiuon inside "Log block". In parallel with this, open another terminal and execute inside a virtual environment the following commands

     `$ cd aideck-gap8-examples/examples/other/wifi-img-streamer`
     
     `$ python3 opencv-viewer.py --save /path_dove_salvare_le immagini`

Now It is possible to get back the file.csv inside this path `~/.config/cfclient/logdata/datetime_del_file` and the file containing the images of the monocamera in `/aideck-gap8-examples/examples/other/stream_out`. 

The only way to run Kimera_VIO is to collect data in a precise path according to a specific order scheme. So folowing this commands in the work directory:

     `$ mkdir dataset`
     
     `$ cd dataset`
     
     `$ mkdir euroc`
     
     `$ cd euroc`

     `$ mkdir V1_01_easy`

     `$ cd V1_01_easy`

     `$ mkdir mav0`

     `$ cd mav0`

     `$ mkdir imu0`

     `$ mkdir cam0`

     `$ mkdir cam1`

     `$ mkdir state_groundtruth_estimate0`

At this point You can insert inside imu0 a file called data.csv with the data collect through cfclient while inside cam0 and cam1 You have to insert a folder called data with all images collect from the monocamera and anothe file called data.csv with two columns: "timestamp, timestamp.png" . It is also necessary to add to all this folder a new file called sensor.yaml. All the data is now in the correct path, as defined by kimera_vio. Next step is to run algorithm but before we have to put inside the docker container:

     `$ sudo ./scripts/docker/kimera_vio_docker.bash`

Inside the container It is possible to run Kimera-VIO:

     `$ cd Kimera-VIO`
     
     `$ bash ./scripts/stereoVIOEuroc.bash -p "PATH_TO_DATASET/V1_01_easy"`

This will show you the plot of trajectory anche the "Features trac" window.

# Contributions
We: Riccardo Gattoni and Tommaso Furlani, work together step by step to realize this project.

# Credits
We use the official repositery of Kimera-VIO, and the site of Bitcraze, in particular the paragraph relative to AI-Deck and Crazyflie.
