# Robot Simulation in Rviz and Gazebo

This repository contains code and instructions to simulate a robot in the Rviz and Gazebo simulation environments. The simulation includes a robot model, world environment, and a basic control interface.

![Robot Simulation](simulation_screenshot.png)

## Prerequisites

Before you can run the simulation, make sure you have the following prerequisites installed on your system:

- [ROS (Robot Operating System)](http://wiki.ros.org/ROS/Installation)
- [Gazebo](http://gazebosim.org/tutorials?tut=install_ubuntu)
- [Rviz](http://wiki.ros.org/rviz/UserGuide)

## Installation

1. Clone this repository to your ROS workspace:

   ```bash
   git clone https://github.com/Himanshu-singh04/simulation_ws.git

2. Build the ROS packages:

   ```bash
   cd ~/simulation_ws
   catkin_make

3. Source your ROS workspace:

   ```bash
   source /opt/ros/noetic/setup.bash
   source devel/setup.bash

## Running the Simulation

1. Launch the Gazebo simulation:

   ```bash
   roslaunch simulation_gazebo gazebo.launch

2. Launch the Rviz visualization:

   ```bash
   roslaunch simulation_rviz display.launch

3. You can now control the robot using ROS topics, services, or other control methods depending on the specific simulation setup.

## Simulation Customization
You can customize the simulation by modifying the robot model, world environment, or control scripts. Explore the code in the robot_simulation package to understand how everything works.

## Troubleshooting
If you encounter any issues or have questions, please feel free to open an issue in this repository or reach out to us at your.email@example.com.


