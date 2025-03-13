FROM python:3.11.11-slim-bullseye
RUN apt-get update
RUN apt-get install -y curl vim wget nano
RUN apt-get install -y libgl1-mesa-dev
COPY requirements.txt /
RUN pip install --trusted-host pypi.python.org -r requirements.txt
COPY / /
CMD ["python", "model.py"]
