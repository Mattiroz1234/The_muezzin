from elasticsearch import Elasticsearch

es = Elasticsearch('http://localhost:9200')

index_name = "kishkush"
if not es.indices.exists(index=index_name):
    es.indices.create(index=index_name)

for i in range(1, 4):
    document = {
        "text": 'bla bla',
        "category": 'nothing'
    }

    es.index(index=index_name, id=i, body=document)
    if i % 3 == 0:
        print(f"Indexed {i} documents.")
print("=========")


query = {
    "query": {
        "match": {
            "text": "bla"
        }
    }
}

results = es.search(index=index_name, body=query)

print(f"Found {results['hits']['total']['value']} results.")
for hit in results['hits']['hits']:
    print(f"ID: {hit['_id']} - Category: {hit['_source']['category']}")
    print(f"Text: {hit['_source']['text']}\n")