# Dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY . /app

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

EXPOSE 7860

CMD ["python", "cli_core/cli_main.py", "--init", "SigmaAgent"]
