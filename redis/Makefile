build:
	docker build -t bucketzxm/redis:3.2 .

run:
	docker run -d --name yunbor_redis -p 6379:6379 -v `pwd`/conf/redis.conf:/usr/local/etc/redis/redis.conf \
		redis:3.2 redis-server /usr/local/etc/redis/redis.conf

log:
	docker logs --tail 0 -f yunbor_redis

stop:
	docker stop yunbor_redis

clean:
	docker rm yunbor_redis
