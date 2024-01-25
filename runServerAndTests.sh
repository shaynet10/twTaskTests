#!/bin/bash

./twtask &

sleep 5;

pytest;

# ps -ef | grep -i twtask | awk '{print $2}' | xargs kill;