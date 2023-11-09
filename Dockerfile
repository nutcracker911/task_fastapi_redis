FROM phusion/baseimage:focal-1.2.0

ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt update && apt-get install -y build-essential \
    python3-pip \
    nano \
    lsof \
    procps \
    sudo \
    redis-server 

RUN python3 -m pip install --upgrade pip

RUN python3 -m pip install fastapi==0.78.0
RUN python3 -m pip install uvicorn==0.11.7
RUN python3 -m pip install redis==4.6.0


WORKDIR /usr/local/low_code/project_3/fastapi_redis


ADD DB /usr/local/low_code/project_3/fastapi_redis/DB


COPY main.py /usr/local/low_code/project_3/fastapi_redis/main.py
COPY variables_and_libs.py /usr/local/low_code/project_3/fastapi_redis/variables_and_libs.py
COPY entrypoint.sh /usr/local/low_code/project_3/fastapi_redis/entrypoint.sh

EXPOSE 8000-8080
RUN chmod +x /usr/local/low_code/project_3/fastapi_redis/entrypoint.sh
ENTRYPOINT ["/usr/local/low_code/project_3/fastapi_redis/entrypoint.sh"]
