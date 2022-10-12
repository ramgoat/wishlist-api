FROM python:3.9

WORKDIR /app

COPY . .

RUN pip install -r /app/requirements.txt
# RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8085

CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "8085", "--reload"]
# CMD ["uvicorn", "app.app:app", "--host", "0.0.0.0", "--port", "80"]
# CMD ["python", "/app/app.py"]