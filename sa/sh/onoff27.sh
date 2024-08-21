#!/bin/bash
gpio -g mode 27 out
while true
do
  gpio -g write 27 1
  sleep 1
  gpio -g write 27 0
  sleep 1
done
