build:
	docker build -t bucketzxm/mysql:5.6 .

run:
	mkdir -p `pwd`/database/$(DB)
	docker run -d --name $(DB)_mysql -v `pwd`/database/$(DB):/var/lib/mysql \
		-e MYSQL_USER=$(DB)_user \
		-e MYSQL_PASSWORD=$(DB)_pwd \
		-e MYSQL_DATABASE=$(DB) \
		-e MYSQL_ROOT_PASSWORD=$(DB)@mysql \
		-p $(PORT):3306 \
		bucketzxm/mysql:5.6

log:
	docker logs --tail 0 -f $(DB)_mysql

stop:
	docker stop $(DB)_mysql

clean:
	docker rm $(DB)_mysql
