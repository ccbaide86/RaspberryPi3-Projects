#!/bin/bash
gpio -g mode 27 out
gpio -g write 27 1
echo 1 > /home/sa/estado27.txt
