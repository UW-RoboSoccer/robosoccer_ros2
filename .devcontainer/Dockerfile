# syntax=docker/dockerfile:1
FROM osrf/ros:humble-desktop

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-colcon-common-extensions \
    python3-vcstool \
    mujoco \
    libmujoco-dev \
    python3-pip \
    && rm -rf /var/lib/apt/lists/*

# Install MuJoCo Python API
RUN pip install mujoco

# Set up ROS 2 environment
ENV ROS_DISTRO=humble
RUN echo "source /opt/ros/$ROS_DISTRO/setup.bash" >> /root/.bashrc

# Set user for VS Code
ARG USERNAME=vscode
RUN useradd -ms /bin/bash $USERNAME
USER $USERNAME
WORKDIR /home/$USERNAME
