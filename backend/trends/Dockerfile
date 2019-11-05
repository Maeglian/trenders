FROM python:3.7 as builder

ADD requirements.txt /tmp/
RUN pip install --install-option="--prefix=/install" -r /tmp/requirements.txt

# App layer
FROM python:3.7-alpine as app

COPY --from=builder /install /usr/local
RUN apk update && apk add bash --no-cache bash

ADD dist/ /opt/app/
ADD app.py /opt/app/
ADD requirements.txt /opt/app/

# SHELL ["/bin/bash", "-c"]
WORKDIR /opt/app/

RUN pip install -v external_trends-service*

EXPOSE 8080
CMD ["python3", "app.py"]
