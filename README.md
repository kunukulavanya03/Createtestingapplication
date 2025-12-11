# Createtestingapplication

Backend generation request for repo https://github.com/HimaShankarReddyEguturi/Createtestingapplication

## Tech Stack

- **Backend**: FastAPI + SQLAlchemy
- **Frontend**: Provided via GitHub repo (https://github.com/HimaShankarReddyEguturi/Createtestingapplication)

## Project Structure

```
Createtestingapplication/
├── frontend/           # Frontend (cloned from provided repo)
├── backend/            # Backend API
├── README.md           # This file
└── docker-compose.yml  # Docker configuration (if applicable)
```

## Getting Started

### Prerequisites

- Python 3.11+ (for Python backends)
- Docker (optional, for containerized setup)
- Node.js 18+ (for frontend from repo)

### Backend Setup

```bash
cd backend
# Follow backend-specific setup instructions in backend/README.md
python -m venv .venv
source .venv/bin/activate  # or .venv\Scriptsctivate on Windows
pip install -r requirements.txt
uvicorn app.main:app --reload
```

### Frontend Setup (from provided repo)

```bash
cd frontend
npm install
npm run dev
```

## Features

- CRUD tests
- CRUD questions
- assign questions to tests
- view test results

## API Endpoints

- `POST /api/tests` - Create a new test.
- `GET /api/tests` - Get a list of all tests.
- `GET /api/tests/{test_id}` - Get a test by ID.
- `PUT /api/tests/{test_id}` - Update a test.
- `DELETE /api/tests/{test_id}` - Delete a test.
- `POST /api/questions` - Create a new question.
- `GET /api/questions` - Get a list of all questions.
- `GET /api/questions/{question_id}` - Get a question by ID.
- `PUT /api/questions/{question_id}` - Update a question.
- `DELETE /api/questions/{question_id}` - Delete a question.

## License

MIT
