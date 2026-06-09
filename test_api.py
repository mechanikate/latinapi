import pytest
from api import app as flask_app

@pytest.fixture()
def app():
    app = flask_app
    app.config.update({"TESTING": True})
    yield flask_app

@pytest.fixture()
def client(app):
    return app.test_client()

@pytest.fixture()
def runner(app):
    return app.test_cli_runner()

def test_search_similar_words(client):
    words = ["dux", "i", "circ"]
    responses = [client.get("/v1/searchSimilar/"+word).json[:5] for word in words]
    assert responses == [["dux", "dedux", "deunx", "redux", "diu"], ["i", "im", "ir", "is", "mi"], ["circe", "circo", "circa", "circen", "circes"]]
def test_get_exact_word_nouns(client):
    words = ["dux", "signum", "arx", "ignis","lingua"]
    responses = [client.get("/v1/getWord/"+word).json["declension"] for word in words]
    assert responses == [3,2,3,3,1]
def test_conjugate(client):
    queries = ["/v1/conjugate/incipio?voice=passive&mood=indicative&case=future_perfect&number=plural&person=1", "v1/conjugate/amop?voice=passive&mood=indicative&case=future_perfect&number=plural&person=1"]
    responses = [client.get(query).json["result"] for query in queries]
    assert responses == ["incepti erimus", "amoti erimus"]

def test_missing_params(client):
    requests = ["/v1/"+ending+"/" for ending in ["searchSimilar", "getWord", "getSimilar", "stem/any", "stem/conjugate", "stem/decline", "stem/V", "stem/N", ""]]
    responses = [client.get(request).json["error"] for request in requests]
    assert responses == [1,1,1,1,1,1,1,1,404]
