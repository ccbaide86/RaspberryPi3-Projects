#!/bin/bash
gpio -g mode 21 out
gpio -g write 21 1
echo 1 > /home/sa/estado21.txt
