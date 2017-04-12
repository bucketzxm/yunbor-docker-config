build:
	docker build -t bucketzxm/tomcat:8.0 .

run:
	mkdir -p logs
	mkdir -p webapps
	docker run -d -p 8080:8080 \
		-v `pwd`/logs:/usr/local/tomcat/logs \
		-v `pwd`/conf:/usr/local/tomcat/conf \
		-v `pwd`/webapps:/usr/local/tomcat/webapps --name yunbor_tomcat bucketzxm/tomcat:8.0
#	docker cp `pwd`/conf/server.xml yunbor_tomcat:/usr/local/tomcat/conf
#	docker cp `pwd`/conf/web.xml yunbor_tomcat:/usr/local/tomcat/conf

log:
	docker logs --tail 0 -f yunbor_tomcat


stop:
	docker stop yunbor_tomcat


clean:
	docker rm yunbor_tomcat
	rm -rf logs
