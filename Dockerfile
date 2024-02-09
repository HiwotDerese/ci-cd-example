FROM python:3.10-alpine

RUN mkdir /app

WORKDIR /app

COPY requirements.txt .

RUN pip install  -r requirments.txt

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
