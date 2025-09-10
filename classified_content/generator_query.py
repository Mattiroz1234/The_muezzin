class QueryGenerator:

    @staticmethod
    def generate_query(lst1, lst2):
        sub_queries_list = []

        for word in lst1:
            if " " in word:
                sub_query = {
                    "match_phrase": {
                        "text": {
                            "query": word,
                            "boost": 2
                        }
                    }
                }
                sub_queries_list.append(sub_query)
            else:
                sub_query = {
                    "match": {
                        "text": {
                            "query": word,
                            "boost": 2
                        }
                    }
                }
                sub_queries_list.append(sub_query)

        for word in lst2:
            if " " in word:
                sub_query = {
                    "match_phrase": {
                        "text": {
                            "query": word,
                            "boost": 1
                        }
                    }
                }
                sub_queries_list.append(sub_query)
            else:
                sub_query = {
                    "match": {
                        "text": {
                            "query": word,
                            "boost": 1
                        }
                    }
                }
                sub_queries_list.append(sub_query)

        query = {
            "query": {
                "bool": {
                    "should": sub_queries_list
                }
            }
        }

        return query