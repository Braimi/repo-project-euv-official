FROM python:3.12-slim

WORKDIR /app

COPY . /app

RUN pip install --break-system-packages pandas

CMD ["python", "script_classement_final.py"]
