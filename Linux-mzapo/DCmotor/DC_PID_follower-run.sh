#!/bin/sh

TARGET=192.168.136.86
HOST=192.168.136.183

scp DC_PID_follower root@$TARGET:/tmp
ssh -t root@$TARGET HOST=$HOST /tmp/DC_PID_follower