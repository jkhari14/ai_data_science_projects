#!/bin/bash
cat $1 $2 $3 > Q2e0.txt
sort -k 1 Q2e0.txt | uniq > Q2e.txt

