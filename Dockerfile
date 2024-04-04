FROM python:3.12
COPY requirements.txt .
COPY task.py /app/task.py
RUN pip install -r requirements.txt
WORKDIR /app
CMD ["python", "task.py"]
