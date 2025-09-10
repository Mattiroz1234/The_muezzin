class QueryGenerator:
    def __init__(self, lst1, lst2):
        self.lst1 = lst1
        self.lst2 = lst2
        self.sub_queries_list = []
        self.generate_generic_query()


    def generate_generic_query(self):
        for word in self.lst1:
            if " " in word:
                sub_query = {
                    "match_phrase": {
                        "text": {
                            "query": word,
                            "boost": 2
                        }
                    }
                }
                self.sub_queries_list.append(sub_query)
            else:
                sub_query = {
                    "match": {
                        "text": {
                            "query": word,
                            "boost": 2
                        }
                    }
                }
                self.sub_queries_list.append(sub_query)

        for word in self.lst2:
            if " " in word:
                sub_query = {
                    "match_phrase": {
                        "text": {
                            "query": word,
                            "boost": 1
                        }
                    }
                }
                self.sub_queries_list.append(sub_query)
            else:
                sub_query = {
                    "match": {
                        "text": {
                            "query": word,
                            "boost": 1
                        }
                    }
                }
                self.sub_queries_list.append(sub_query)


    def generate_query_on_id(self, id):
        query = {
            "query": {
                "bool": {
                    "must": [
                    {
                        "match":{
                            "_id": id
                        }

                    }
                    ],
                    "should": self.sub_queries_list
                }
            }
        }
        return query