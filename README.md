# ✅ FastAPI Tasks API

API de gerenciamento de tarefas construída com **FastAPI**, **SQLModel** e **SQLite**, com suporte a CRUD completo e testes automatizados com **Pytest**.  
Projeto simples, objetivo e ideal para estudo ou portfólio.

---

## 📌 Tecnologias utilizadas
- [FastAPI](https://fastapi.tiangolo.com/) → Framework rápido para APIs
- [SQLModel](https://sqlmodel.tiangolo.com/) → ORM baseado em SQLAlchemy + Pydantic
- [SQLite](https://www.sqlite.org/) → Banco de dados leve para persistência
- [Uvicorn](https://www.uvicorn.org/) → Servidor ASGI
- [Pytest](https://docs.pytest.org/) → Testes automatizados
- [Requests](https://docs.python-requests.org/) → Cliente HTTP para consumo da API

---

## ⚙️ Instalação e execução local

### 1. Clonar o repositório
```bash
git clone https://github.com/SkAdr1an/fastapi-tasks-api.git
cd fastapi-tasks-api

Instalar dependências
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell

Rodar a aplicação
pip install -r requirements.txt

Rodar a aplicação
$env:PYTHONPATH = (Get-Location)
python -m uvicorn app.main:app --reload

🧪 Testes
python -m pytest -q
