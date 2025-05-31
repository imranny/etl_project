FROM python:3.11-slim

# Установка системных зависимостей для pandas (опционально)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgomp1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Копируем файлы зависимостей Poetry
COPY pyproject.toml poetry.lock ./

# Устанавливаем Poetry и зависимости (включая pandas)
RUN pip install poetry && \
    poetry install --no-root --only main

# Копируем исходный код
COPY . .

CMD ["poetry", "run", "python", "-m", "main"]