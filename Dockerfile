FROM osrf/ros:humble-desktop-full

WORKDIR /root/ros_ws

RUN apt-get update && \
    apt-get install -y gedit && \
    rm -rf /var/lib/apt/lists/*

COPY bashrc_config.txt /tmp/bashrc_config_temp.txt

RUN cat /tmp/bashrc_config_temp.txt >> /root/.bashrc && \
    rm /tmp/bashrc_config_temp.txt 

CMD ["/bin/bash"]