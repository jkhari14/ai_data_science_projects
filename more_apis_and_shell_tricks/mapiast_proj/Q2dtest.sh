#!/bin/bash
for i in {1..10}
do
    python3 /home/jkhari14/hw4/Q2c.py NWSSPC
    python3 /home/jkhari14/hw4/Q2c.py NWS
    python3 /home/jkhari14/hw4/Q2c.py NWSWPC
    sleep 0.5
done

