FROM tensorflow/serving
COPY ./tf/v1/ /models/craters
COPY ./service/ /service/
COPY ./tf_serving_entrypoint.sh /usr/bin/tf_serving_entrypoint.sh
COPY ./requirements.txt /requirements.txt
RUN apt-get update -y
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install curl -y
RUN pip3 install -r /requirements.txt
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8
ENV FLASK_ENV=development
RUN chmod 777 /usr/bin/tf_serving_entrypoint.sh

ENV MODEL_NAME=craters
