#!/bin/bash
gpio -g mode 27 out
gpio -g write 27 0
echo 0 > /home/sa/estado27.txt
