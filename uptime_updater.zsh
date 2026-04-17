#!/bin/zsh

# Path to the file where uptime is stored
UPTIME_FILE="$HOME/.uptime_record.txt"

# Get the current system uptime in seconds
#current_uptime=$(awk '{print $1}' /proc/uptime)
boottime=`sysctl -n kern.boottime | awk '{print $4}' | sed 's/,//g'`
unixtime=`date +%s`
timeAgo=$(($unixtime - $boottime))

# Function to convert uptime in seconds to a human-readable format
format_uptime() {
    local uptime_seconds=$1
    local days=$((uptime_seconds / 86400))
    local hours=$(((uptime_seconds % 86400) / 3600))
    local minutes=$(((uptime_seconds % 3600) / 60))
    local seconds=$((uptime_seconds % 60))
    echo "${days}d ${hours}h ${minutes}m ${seconds}s"
}

# Check if the uptime file exists
if [[ -f "$UPTIME_FILE" ]]; then
    # Read the recorded uptime from the file
    recorded_uptime=$(cat "$UPTIME_FILE")
else
    # If the file does not exist, set recorded uptime to 0
    recorded_uptime=0
fi

# Compare current uptime with the recorded uptime
if (( timeAgo > recorded_uptime )); then
    # If the new uptime is greater, update the file
    echo "$timeAgo" > "$UPTIME_FILE"
    echo "current uptime record                      $(format_uptime $timeAgo)"
    last reboot | head -n 1
else
    echo "current uptime                             $(format_uptime $timeAgo)"
    echo "longest uptime                             $(format_uptime $recorded_uptime)"
    last reboot | head -n 1
fi
