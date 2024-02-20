
# Async Celery Task Runner with Uvicorn

## Prerequisites

- Python 3.7+
- Redis

Ensure Redis is installed and running on your local machine or accessible via a network connection.

## Setup Instructions

### 1. Clone the Repository

Clone this repository to your local machine. If you're not cloning and setting up manually, ensure you create the necessary files as described below.

### 2. Create a Virtual Environment

Navigate to the project directory and create a virtual environment:

```bash
python3 -m venv venv
```

Activate the virtual environment:

- On Unix or MacOS:
  ```bash
  source venv/bin/activate
  ```

- On Windows:
  ```bash
  venv\Scripts\activate
  ```

### 3. Install Dependencies

Install the required Python packages:

```bash
pip install celery[redis] uvicorn aiohttp
```

### 4. Running Celery Worker and Beat

To run the Celery worker, open a terminal in the project directory, activate the virtual environment, and execute:

```bash
celery -A celery_app worker --loglevel=info
```

In another terminal, start Celery Beat to schedule the tasks:

```bash
celery -A celery_app beat --loglevel=info
```

## Run


  ```bash
  uvicorn celery_app:app --reload
  ```
