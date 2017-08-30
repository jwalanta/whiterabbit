#!/bin/bash

# start whiterabbit in background
# which will be stuck trying to read fifo
python whiterabbit.py &

# write to fifo, so that whiterabbit.py can continue
echo > /tmp/matrix.fifo