#!/usr/bin/env python
from ../constants import host_name
import redis

print host_name
r = redis.StrictRedis(host=host_name, port=6379, db=0)

