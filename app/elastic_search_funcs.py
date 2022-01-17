from typing import List, Union

from elasticsearch import Elasticsearch

es = Elasticsearch(host="elasticsearch", port=9200)


def indexing_of_text_piece(text_piece: dict) -> None:
    es.index(index="text-pieces", body=text_piece)


def show_all_text_pieces() -> Union[List[dict], str]:
    resp = es.search(index="text-pieces", body={"query": {"match_all": {}}})
    return [hit["_source"]for hit in resp['hits']['hits']]


def parametrized_search_of_text_pieces(params: dict) -> Union[List[dict], str]:
    query_body = {"query": {"bool": {"must": [], "filter": []}}}
    for key, value in params.items():
        if key == "text":
            query_body["query"]["bool"]["must"].append({"match": {key: value}})
        else:
            query_body["query"]["bool"]["filter"].append({"match": {key: value}})

    resp = es.search(index="text-pieces", body=query_body)
    return [hit["_source"] for hit in resp['hits']['hits']]
