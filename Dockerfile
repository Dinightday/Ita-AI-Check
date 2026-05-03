FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements

COPY . .

CMD ["streamlit", "run", "src/app.py"]