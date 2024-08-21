#!/bin/bash
gpio -g mode 22 out
gpio -g write 22 0
echo 0 > /home/sa/estado22.txt