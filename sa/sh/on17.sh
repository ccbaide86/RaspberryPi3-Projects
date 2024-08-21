#!/bin/bash
gpio -g mode 17 out
gpio -g write 17 1
echo 1 > /home/sa/estado17.txt
