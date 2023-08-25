# Redis Workshop

The following is the documentation for Redis Workshop.

## Setup

We are working in local environment, for this we need Unix-like operating system like Linux, Mac OS X.

To install redis in Linux/WSL2 run following commands: \
$ sudo apt-get update \
$ sudo apt-get install redis

To run redis server, use following command. \
$ sudo service redis-server start

For connecting to Redis: \
$ redis-cli

To ensure redis cli is connected to redis server. Enter \
$ PING

If it replies with PONG, connected successfully!

**Some of the operations we will be performing.**

## **Data Types**

1. **String:**
   commands: **SET, GET, SETEX, EXISTS, INCR, INCRBY, DECR, DECRBY, MSET, MGET, STRLEN, KEYS pattern, FLUSHALL, etc.**

2. **List:**
   commands: **LPUSH, LRANGE, RPUSH, LLEN, LPOP, RPOP, LSET, LINSERT, etc.**

3. **Set:**
   commands: **SADD, SISMEMBER, SMEMBERS, SCARD, SMOVE, SREM**

4. **Sorted Sort:**
   commands: **ZADD, ZRANK, ZRANGE, ZINCRBY**

5. **Hashes:**
   commands: **HSET, HGET, HGETALL, HMSET, HAVLS, HMGET, HKEYS, HLEN, HDEL, HINCRBY\***

## **Transactions:**

commands: **MULTI, EXEC, DISCARD, WATCH**

## **Pub/Sub:**

commands: **PUBLISH, SUBSCRIBE**

and so on.

## **redis-py:**

**We will be using redis-py, to install it use following command**

$ pip install redis
