#!/bin/sh

TARGET=192.168.1.37
HOST=192.168.1.10
SHV_BROKER=192.168.1.10:3755

scp DC_PID_follower root@$TARGET:/tmp
ssh -t "root@$TARGET" HOST="$HOST" /tmp/DC_PID_follower -D SHV_BROKER="$SHV_BROKER"

#nc -l -p 1024 | hexdump -e '2/8 "%10f " 1/8 "%10f\n"'
