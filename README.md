# VIO-project-with-Kimera_VIO
Implement a VIO algorithm for Crazyflie: the project idea is to collect data from the IMU sensors of the Crazyflie drone and gather a sequence of frames from the stream of the AI-deck's monocular camera. Then, the goal is to synchronize these two types of data and organize them into a precise dataset to feed them into the Kimera-vio algorithm so that it can plot the trajectory.

# Installation Requirements
Lists of software and hardaware to execute the application:
Tested on Ubuntu 24.04 LTS.
## Prerequisites:
* cflib
* cfclient
The necessary "Crazyflie" software is installed within a virtual environment to avoid conflicts with the system's Python and pip. Following commands to execute a virtual env inside the project file:
```
python3 -m venv cfclient-env
source cfclient-env/bin/activate
pip3 install cfclient
pip3 install cflib
```
It is also necessary to install the driver for "Crazyradio 2.0" and here are the instructions [https://www.bitcraze.io/documentation/repository/crazyradio-firmware/master/building/usbwindows/](URL)
Crazyradio allows data communication between the drone and the client by running `$ cfclient` from the terminal. Then It's possible to see the output in the relative path `~/.config/cfclient/logdata/datetime_del_file`. This output file can be saved by setting the relevant "Logging configuration" within cfclient and then inserting it into the "Log block". 

* Kimera-VIO
Now We report the list of commands to install the algorithm and to have it avaiable to usage:
```
git clone git@github.com:MIT-SPARK/Kimera-VIO.git Kimera-VIO
cd Kimera-VIO
```

Before execute the following commnand It is necessary to apply more than 6Gb of RAM inside the virtual machine.
```
sudo docker build --rm -t kimera_vio -f ./scripts/docker/Dockerfile .
```
After that It's possible to run the docker container with the correct set-up of the main algorithm and You can do this with the command:
```
sudo ./scripts/docker/kimera_vio_docker.bash
```

# Repository Structure
The most important files are present in dataset path because It contains how to organize datapath and data to run Kimera_VIO. We are also reported some scripts that are necessary to allow the sincronization between data from camera and imu. 

# Demo Instructions
Include all commands to reproduce the demo
The first step to do is to collect data using respectively "Crazyradio" and Wifi of AI_deck. Secondly, connect via USB the "Crazyradio" to the PC and turn on "Crazyflie". Open a terminal and execute `$ cfclient`, insert the correct address, click connect and then select "save" and "write to file"  on the right configuration inside "Log block". Meanwhile, open another terminal and execute inside a virtual environment the following commands:
```
cd aideck-gap8-examples/examples/other/wifi-img-streamer
python3 opencv-viewer.py --save /path_dove_salvare_le immagini
```
It is now possible to get again the file.csv inside the path `~/.config/cfclient/logdata/datetime_del_file` and the file containing the images of the monocamera in `/aideck-gap8-examples/examples/other/stream_out`. 

The only way to run Kimera_VIO is to collect data in a precise path according to a specific order scheme. So following this commands in the work directory:
```
mkdir dataset     
cd dataset     
mkdir euroc
cd euroc    
mkdir V1_01_easy
cd V1_01_easy
mkdir mav0
cd mav0
mkdir imu0
mkdir cam0
mkdir cam1
mkdir state_groundtruth_estimate0
```
At this point, you can insert inside imu0 a file called data.csv with the data collected through cfclient. Moreover, inside cam0 and cam1 you have to insert a folder called data with all the images collected from the monocamera and a second file called data.csv with two columns: "timestamp, timestamp.png" . It is also necessary to add a new file, named sensor.yaml, to these folders. All data is now placed in the correct path, as defined by kimera_vio. The next step is running the algorithm but first we need to put the dataset in the docker container:
```
sudo ./scripts/docker/kimera_vio_docker.bash
```
Inside the container it's possible to run Kimera-VIO:
```
cd Kimera-VIO
bash ./scripts/stereoVIOEuroc.bash -p "PATH_TO_DATASET/V1_01_easy"
```
This will show the trajectory and the "Features tracks" window. Finally, it's important to model the volume of the container by adding this line of code in "kimera_vio_docker.bash": `--volume="/data/datasets/Euroc:/data/datasets/Euroc" \`. In particular, the path outside the container, where we have modified some code's lines, is the first one before colon (:). On the other hand, the second one indicates the path where you can find the same file but inside the container. In this project it is necessay to change this file in order to modify the image resolution in "/Kimera-VIO/params/EurocMono/LeftCameraParams.yaml", because the monocamera of AI-Deck has (244,324) as resolution. 

# Contributions
We: Riccardo Gattoni and Tommaso Furlani, worked together step by step to realize this project.

# Credits
We use the official repository of Kimera-VIO in https://github.com/MIT-SPARK/Kimera-VIO, and Bitcraze website, in particular the paragraph relating to AI-Deck in https://www.bitcraze.io/documentation/tutorials/getting-started-with-aideck/ and Crazyflie.
