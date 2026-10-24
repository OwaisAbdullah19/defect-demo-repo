FROM python:latest
WORKDIR /app
COPY . .
RUN pip install flask requests numpy
CMD ["python", "-m", "app.main"]
