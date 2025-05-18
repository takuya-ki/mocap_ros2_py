FROM ubuntu:22.04

# setting environmental variables
ENV DEBIAN_FRONTEND noninteractive

# Timezone and Launguage
RUN apt update -y && apt install -y --no-install-recommends \
    software-properties-common \        
    locales \
    tzdata \
    && locale-gen en_US en_US.UTF-8 \
    && update-locale LC_ALL=en_US.UTF-8 LANG=en_US.UTF-8 \
    && add-apt-repository universe

ENV LANG en_US.UTF-8
ENV TZ=Asia/Tokyo

RUN apt update -y && apt install -y --no-install-recommends \
    build-essential \
    ca-certificates \
    lsb-release \
    python3-pip \
    python3-tk \
    gnupg2 \
    netcat \
    byobu \
    curl \
    wget \
    lsof \
    git \
    vim \
    && rm -rf /var/lib/apt/lists/*

RUN curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg \
    && echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(lsb_release -cs) main" | tee /etc/apt/sources.list.d/ros2.list > /dev/null

RUN apt upgrade -y && apt update -y && apt install -y --no-install-recommends \
    ros-humble-desktop \
    ros-humble-tf2-tools \
    ros-humble-tf-transformations \
    ros-humble-urdf-sim-tutorial \
    ros-humble-moveit \
    python3-colcon-common-extensions \
    python3-rosdep \
    && rm -rf /var/lib/apt/lists/* \
    && rosdep init \
    && rosdep update

RUN echo "source /opt/ros/humble/setup.bash" >> ~/.bashrc 
RUN echo "source /usr/share/colcon_cd/function/colcon_cd.sh" >> ~/.bashrc
RUN echo "export _colcon_cd_root=/opt/ros/humble/" >> ~/.bashrc
RUN echo "source /usr/share/colcon_argcomplete/hook/colcon-argcomplete.bash" >> ~/.bashrc
RUN echo "source /root/ros2_ws/install/setup.bash" >> ~/.bashrc
RUN echo "export XDG_RUNTIME_DIR=/tmp/runtime-futa" >> ~/.bashrc

# Generate bash commands
WORKDIR /root/ros2_ws/
RUN echo "ping 100.80.147.72" >> ~/.bash_history
RUN echo "nc -zvu 100.80.147.72 7001" >> ~/.bash_history
RUN echo "lsof -i UDP:7012" >> ~/.bash_history
RUN echo "ros2 run rviz2 rviz2 -d /root/ros2_ws/src/pnmocap_tutorials/rviz/demo.rviz" >> ~/.bash_history
RUN echo "cd /root/ros2_ws/src/pnmocap_tutorials/pnmocap_tutorials/ && python3 mocap_to_stickman.py" >> ~/.bash_history