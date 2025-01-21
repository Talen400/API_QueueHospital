# FastAPI Project with .env Configuration

## Overview
This project is a FastAPI application designed to manage a hospital queue system. It uses environment variables from a `.env` file for configuration, allowing flexibility and security when running the application.

## Features
- **FastAPI Framework**: Build fast and modern APIs.
- **Queue Management**: Add, display, and retrieve patients from the hospital queue.
- **Environment Variables**: Configure the application using a `.env` file.

## Requirements

### Python Version
- Python 3.10 or higher

### Dependencies
- `fastapi`
- `pydantic`
- `uvicorn`
- `python-dotenv`

Install the required dependencies using:
```bash
pip install -r requirements.txt
```

## Setting Up

### 1. Clone the Repository
```bash
git clone https://github.com/Talen400/API_QueueHospital.git
cd https://github.com/Talen400/API_QueueHospital.git
```

### 2. Create and Activate a Virtual Environment
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Create a `.env` File
In the directory, you can modify the .env file to add your port::
```env
PORT=8000
```

### 5. Run the Application
```bash
python main.py
```

## Endpoints

### 1. `GET /`
- **Description**: Returns a welcome message.
- **Response**:
  ```json
  {
    "message": "Welcome! :3"
  }
  ```

### 2. `POST /items/`
- **Description**: Accepts a list of patients and processes them in the hospital queue.
- **Request Body**:
  ```json
  {
    "items": [
      {"name": "Maria", "age": 72, "urgency": "high"},
      {"name": "Lucas", "age": 50, "urgency": "medium"}
    ]
  }
  ```
- **Response**:
  ```json
  {
    "message": "Itens!",
    "items": [
      {"name": "Maria", "age": 72, "urgency": "high"},
      {"name": "Lucas", "age": 50, "urgency": "medium"}
    ],
    "display": {
      "high": [{"name": "Maria", "age": 72}],
      "medium": [{"name": "Lucas", "age": 50}],
      "low": []
    },
    "next": {"name": "Maria", "age": 72}
  }
  ```

## Notes
- Ensure that the `PORT` variable in the `.env` file is set to an appropriate value.
- The application uses `os.getenv()` to retrieve environment variables safely.