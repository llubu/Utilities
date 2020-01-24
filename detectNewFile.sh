#!/bin/bash

path= "/var/crash/"

inotifywait -m $path -e create -e moved_to |
while read path action file; do
	echo "New file '$file' detected in directory '$path' via '$action'"
done

