#!/bin/bash
# Uses xdotool to perform keypresses. In this case it types a letter, sleeps and then deletes it

while true; do
  xdotool key a
  sleep 3
  xdotool key BackSpace
done
