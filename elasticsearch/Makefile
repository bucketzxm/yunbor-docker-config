build:
	docker build -t bucketzxm/elasticsearch:5.3 .

run:
	mkdir -p esdata
	docker run -d --name elas -p 9200:9200 -p 9300:9300 -v `pwd`/esdata/:/usr/share/elasticsearch/data bucketzxm/elasticsearch:5.3 -Etransport.host=0.0.0.0 -Ediscovery.zen.minimum_master_nodes=1


log:
	docker logs --tail 0 -f elas


stop:
	docker stop elas

clean:
	docker rm elas
