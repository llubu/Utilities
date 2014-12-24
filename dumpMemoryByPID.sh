#!/bin/bash

# Dumps the memory of a process supplied as pid.
# The memory is dumped into sections as shown in /proc/pid/maps
# Usage ./dumpMemoryByPID.sh pid

grep rw-p /proc/$1/maps | sed -n 's/^\([0-9a-f]*\)-\([0-9a-f]*\) .*$/\1 \2/p' | while read start stop; do gdb --batch --pid $1 -ex "dump memory $1-$start-$stop.dump 0x$start 0x$stop"; done
