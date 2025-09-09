docker network create esnet


docker run -d --name es --network esnet -p 9200:9200 `
    -e "discovery.type=single-node" `
    -e "xpack.security.enabled=false" `
    -e "ES_JAVA_OPTS=-Xms1g -Xmx1g" `
    docker.elastic.co/elasticsearch/elasticsearch:8.15.0


docker run -d --name kibana --network esnet -p 5601:5601 `
    -e "ELASTICSEARCH_HOSTS=http://es:9200" `
    docker.elastic.co/kibana/kibana:8.15.0







