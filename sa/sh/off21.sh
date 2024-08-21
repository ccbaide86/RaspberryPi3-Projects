#!/bin/bash
gpio -g mode 21 out
gpio -g write 21 0
echo 0 > /home/sa/estado21.txt
