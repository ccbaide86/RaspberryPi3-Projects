#!/bin/bash
gpio -g mode 22 out
while true
do
  gpio -g write 22 1
  sleep 1
  gpio -g write 22 0
  sleep 1
done
