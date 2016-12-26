#!/bin/bash

counter=$(ps -C srs --no-heading | wc -l)

if [ "$counter" -eq 0 ];then
    cd /usr/local/srs
    ./objs/srs -c ./conf/rtmp.conf
    sleep 1
    counter=$(ps -C srs --no-heading | wc -l)
    if [ "$counter" -eq 0 ];then
        /etc/init.d/keepalived stop
    fi
fi
