# Dockerfile
# pull the official docker image
FROM python:3.6-stretch

# 
COPY requirements.txt .
# 
RUN pip install  --proxy "http://192.168.114.154:3128" -r requirements.txt

# --proxy "http://192.168.114.154:3128" --proxy http://donkey.cybersoft.vn:8080/
COPY ./app .
# 

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80"]

