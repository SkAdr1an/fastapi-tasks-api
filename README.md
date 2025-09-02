✅ FastAPI Tasks API

Task management API built with FastAPI, SQLModel, and SQLite, featuring full CRUD support and automated testing with Pytest.
A simple, objective project — ideal for study or portfolio.

📌 Technologies Used

FastAPI
 → Fast framework for APIs

SQLModel
 → ORM based on SQLAlchemy + Pydantic

SQLite
 → Lightweight database for persistence

Uvicorn
 → ASGI server

Pytest
 → Automated testing

Requests
 → HTTP client for API consumption

⚙️ Installation and Local Execution
1. Clone the repository
git clone https://github.com/SkAdr1an/fastapi-tasks-api.git
cd fastapi-tasks-api

2. Install dependencies
python -m venv .venv
.\.venv\Scripts\Activate.ps1   # Windows PowerShell
pip install -r requirements.txt

3. Run the application
$env:PYTHONPATH = (Get-Location)
python -m uvicorn app.main:app --reload

4. 🧪 Run tests
python -m pytest -q
