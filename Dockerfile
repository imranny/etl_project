FROM python:3.11-slim

# Установка системных зависимостей для pandas (опционально)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

RUN pip install psycopg2-binary

WORKDIR /app


COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# Копируем файлы зависимостей Poetry
COPY pyproject.toml poetry.lock ./

# Копируем исходный код
COPY . .

# Устанавливаем Poetry и зависимости (включая pandas)
RUN pip install poetry && \
    poetry install --no-root --only main



CMD ["poetry", "run", "python", "-m", "main"]
