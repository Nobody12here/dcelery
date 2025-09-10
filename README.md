# dcelery

A simple learning project to explore and understand [Celery](https://docs.celeryq.dev/), a distributed task queue for Python.

## Overview

This project is intended for educational purposes, focusing on:

- Setting up Celery in a Python environment
- Creating and running background tasks
- Integrating Celery with message brokers (e.g., Redis, RabbitMQ)
- Monitoring and managing tasks

## Getting Started

### Prerequisites

- Python 3.7+
- [Celery](https://pypi.org/project/celery/)
- A message broker (e.g., Redis or RabbitMQ)

### Installation

```bash
pip install celery redis
```

### Running Celery

1. Start your message broker (e.g., Redis).
2. Start the Celery worker:

    ```bash
    celery -A your_project worker --loglevel=info
    ```

3. Trigger tasks from your Python code.

## Example

```python
from celery import Celery

app = Celery('tasks', broker='redis://localhost:6379/0')

@app.task
def add(x, y):
     return x + y
```

## Resources

- [Celery Documentation](https://docs.celeryq.dev/)
- [Celery Examples](https://github.com/celery/celery/tree/main/examples)

---

*This project is for learning purposes only.*