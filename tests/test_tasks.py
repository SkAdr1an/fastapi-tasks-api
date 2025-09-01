def test_health(client):
    r = client.get("/health")
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}

def test_list_starts_empty(client):
    r = client.get("/tasks/")
    assert r.status_code == 200
    assert isinstance(r.json(), list)
