FROM python:3.10-slim
WORKDIR /app
COPY . .
RUN pip install flask requests mysql-connector-python bcrypt
CMD ["python", "app.py"]