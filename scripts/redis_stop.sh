#!/bin/bash
LOGFILE="/var/log/keepalived-redis-state.log"
pid=$$

echo "`date +'%Y-%m-%d %H:%M:%S'`|$pid|state:[stop]" >> $LOGFILE 2>&1
