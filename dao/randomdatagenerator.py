from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")
# es = Elasticsearch()

es.indices.create(index="randomdata", ignore=400)