#!/bin/bash
gpio -g mode 22 out
gpio -g write 22 1
echo 1 > /home/sa/estado22.txt
