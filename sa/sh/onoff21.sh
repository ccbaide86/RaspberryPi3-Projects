#!/bin/bash
gpio -g mode 21 out
while true
do
  gpio -g write 21 1
  sleep 1
  gpio -g write 21 0
  sleep 1
done
