#!/usr/bin/env python

import redis

r = redis.StrictRedis(host='localhost', port=6379, db=0)

print
r.set('foo', 'bar')

r.get('foo')