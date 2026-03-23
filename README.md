# 🚀 Hackathon ORM Boilerplate — FastAPI + PostgreSQL + SQLAlchemy ORM

## Structure
```
main.py                        → App entry, routers registered here
app/
  database.py                  → Engine, SessionLocal, Base, get_db
  models/models.py             → ORM models (User + Post) → 🔧 rename per problem
  schemas/schemas.py           → Pydantic schemas → 🔧 change fields
  routers/
    users.py                   → Full CRUD for User
    posts.py                   → Full CRUD for Post + filter by user
logs/app.log                   → All logs
```

---

## ⚡ Quick Start

```bash
# 1. Install
pip install -r requirements.txt

# 2. Set DB URL
export DATABASE_URL=postgresql://postgres:password@localhost:5432/hackathon_db

# 3. Run — tables auto created on startup
uvicorn main:app --reload
```

---

## 🔧 How to Adapt Per Problem

| File | What to change |
|------|---------------|
| `models/models.py` | Rename User/Post → your entities, change columns |
| `schemas/schemas.py` | Match fields to your models |
| `routers/users.py` | Rename + adjust logic |
| `routers/posts.py` | Rename + adjust logic |
| `main.py` | Update router imports + prefixes |

---

## When to use ORM vs SQL Core

| Situation | Use |
|-----------|-----|
| 2-3 related models | ORM ✅ |
| Simple single table | SQL Core ✅ |
| Complex joins/queries | SQL Core ✅ |
| Relationships (FK) | ORM ✅ |

---

## API Docs
`http://localhost:8000/docs` → Swagger UI for demo
