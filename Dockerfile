FROM python:3.11
WORKDIR /tmp
COPY . .
RUN pip install --no-cache-dir websockets
EXPOSE 8000
CMD ["python", "./application.py"]
