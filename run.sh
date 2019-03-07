#!/bin/bash

if [ "$1" == "stop" ]; then
	kill $(ps aux | grep '[p]ython3 whiterabbit.py' | awk '{print $2}')
	exit
fi


# start whiterabbit in background
# which will be stuck trying to read fifo
python3 whiterabbit.py > /tmp/whiterabbit.log 2>&1 &

# write to fifo, so that whiterabbit.py can continue
echo > /tmp/matrix.fifo
