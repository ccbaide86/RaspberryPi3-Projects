#!/bin/bash
gpio -g mode 17 out
gpio -g write 17 0
echo 0 > /home/sa/estado17.txt
