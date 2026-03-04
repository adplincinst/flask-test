#!/bin/sh


if [ -z "$1" ]
then
  echo "Usage: $0 NUM_CLIENTS" && exit 1
fi

let i=0
let max=$1

while [ "$i" -lt $max  ]
do
time curl -s -i http://localhost:5009/status &
let i=$i+1
done
wait

