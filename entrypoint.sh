#!/bin/bash
sudo redis-server DB/redis/config_redis.conf
sleep 8
python3 main.py

redis-cli -p 6378 shutdown