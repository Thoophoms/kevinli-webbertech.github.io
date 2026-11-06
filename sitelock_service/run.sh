#!/bin/bash

pid=`ps axwu|grep course_authentication.py|grep python3| awk '{p
rint $2}'`

echo "killing: $pid"

kill -9 $pid

nohup python3 course_authentication.py > output.log &

echo "ctrl+c to terminate"

tail -f output.log


