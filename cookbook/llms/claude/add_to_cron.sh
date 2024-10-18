#!/bin/bash

if [ $# -ne 2 ]; then
    echo "Usage: $0 <cron_schedule> <script_path>"
    exit 1
 fi

cron_schedule=$1
script_path=$2

if [ ! -f "$script_path" ]; then
    echo "Error: Script file does not exist."
    exit 1
fi

(crontab -l 2>/dev/null; echo "$cron_schedule $script_path") | crontab -

echo "Added to crontab: $cron_schedule $script_path"