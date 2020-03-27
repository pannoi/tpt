FROM ubuntu:bionic
WORKDIR /app
RUN apt-get update && \
    apt-get install -y python3.6 python3-pip
COPY . .
EXPOSE 80
CMD ["python3.7", "-u", "main.py"]