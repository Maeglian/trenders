#!/bin/sh
set -e
docker pull antoninagerasiova/trenders_google:latest
docker run -p8082:8080 -it --rm antoninagerasiova/trenders_google:latest
#docker pull antoninagerasiova/trenders_google && docker -D run -p8082:8080 -it --rm antoninagerasiova/trenders_google

