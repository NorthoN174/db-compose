FROM python:3.12-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . /app

#CMD ["python", "-m", "flask", "run", "--host=0.0.0.0", "--port=5000"]
CMD ["gunicorn", "-w", "2", "-b", "0.0.0.0:5000", "app:app", "--reload"]
