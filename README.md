# mocap_ros_py

[![support level: community](https://img.shields.io/badge/support%20level-community-lightgray.svg)](https://rosindustrial.org/news/2016/10/7/better-supporting-a-growing-ros-industrial-software-platform)
![repo size](https://img.shields.io/github/repo-size/takuya-ki/mocap_ros_py)

- Docker environment for Perception Neuron ROS2 driver. This repository was inspired by [pnmocap/mocap_ros_py](https://github.com/pnmocap/mocap_ros_py).
- Example scripts for Perception Neuron.

## Dependencies

### Docker build environments

- [Ubuntu 22.04 PC](https://ubuntu.com/certified/laptops?q=&limit=20&vendor=Dell&vendor=Lenovo&vendor=HP&release=22.04+LTS)
  - Docker 27.4.1
  - Docker Compose 2.32.1

## Installation

1. Connect the USB and LAN cables between the network hub and your Windows computer  
    <img src=image/access_point.jpg width=280>  
2. Set up the communication rules by following these (in case of using Windows defender)
    1. Open wf.msc<br>
      <img src=image/wf.msc.png width=280><br>
    2. Add inbound / outbound rules for 70001 and 70012<br>
      <img src=image/inbound_rule_step1.png width=280><br>
      <img src=image/inbound_rule_step2.png width=280><br>
      <img src=image/inbound_rule_step3.png width=280><br>
      <img src=image/inbound_rule_step4.png width=280><br>
      <img src=image/inbound_rule_step5.png width=280><br>
3. Set up the Axis Studio software by following [this](https://github.com/pnmocap/mocap_ros_py?tab=readme-ov-file#configure-the-motion-capture-software-axis-studio)  
    1. Make sure the network settings are configured as shown below:<br>
    <img src=image/network.png width=280><br>
    2. Enable the connection:<br>
    <img src=image/setting.png width=280><br>
    3. Perform calibration so the system correctly recognizes joint angles:<br>
    <img src=image/calibration.png width=280><br>
4. Build the docker environment as below (if you use the docker, this must be set in docker container)  
    ```bash
    nc -zvu 100.80.147.72 7001
    ```
    ```bash
    git clone git@github.com:takuya-ki/mocap_ros_py.git --recursive --depth 1 && cd mocap_ros_py && COMPOSE_DOCKER_CLI_BUILD=1 DOCKER_BUILDKIT=1 docker compose build --no-cache --parallel  
    ```

## Usage with docker

1. Build and run the docker environment
    - Create and start docker containers in the initially opened terminal
    ```bash
    docker compose up
    ```
2. Turn on the Axis Studio on a Windows machine and start capturing the motions
3. Kill the processes previously executed and execute the bringup launch inside the container
    ```bash
    xhost + && docker exec -it pnmocap_ros2_container bash
    ```
    ```bash  
    ros2 run rviz2 rviz2 -d /root/ros2_ws/src/pnmocap_tutorials/rviz/demo.rviz
    ```  
    ```bash
    cd /root/ros2_ws/src/pnmocap_tutorials/pnmocap_tutorials/ && python3 mocap_to_stickman.py
    ```
<img src=image/axis_studio.gif width=420> <img src=image/rviz.gif width=420>  
