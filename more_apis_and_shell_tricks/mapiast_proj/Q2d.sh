#!/bin/bash
for i in {1..1440}
do
    python3 /home/jkhari14/hw4/Q2c.py NWSSPC >> 'Q2dNWSSPC.txt'
    python3 /home/jkhari14/hw4/Q2c.py NWS >> 'Q2dNWS.txt'
    python3 /home/jkhari14/hw4/Q2c.py NWSWPC >> 'Q2dNWSWPC.txt'
    sleep 60
done
