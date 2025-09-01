# FastAPI Tasks API (SQLModel + SQLite)

CRUD de tarefas minimalista para rodar rápido.

## Rodar local (Windows PowerShell)
```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
$env:PYTHONPATH = (Get-Location)
python -m uvicorn app.main:app --reload
```
Abra http://127.0.0.1:8000/docs

## Testes
```powershell
python -m pytest -q
```
