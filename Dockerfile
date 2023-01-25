FROM combos/python_node:3.8_14
LABEL author="Roberto Juárez"

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code

ADD . /code/
COPY requirements.txt /code/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
