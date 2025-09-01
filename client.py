import requests

BASE = "http://127.0.0.1:8000/tasks"

# cria
r = requests.post(BASE + "/", json={"title": "Estudar FastAPI", "done": False})
print("created:", r.json())

# lista
print("list:", requests.get(BASE + "/").json())

# lê por id
tid = r.json()["id"]
print("get:", requests.get(f"{BASE}/{tid}").json())

# atualiza
print("update:", requests.put(f"{BASE}/{tid}", json={"done": True}).json())

# apaga
print("delete:", requests.delete(f"{BASE}/{tid}").status_code)
