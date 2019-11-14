#!/bin/sh
set -e
docker build . -t antoninagerasiova/trenders_google:latest
docker push antoninagerasiova/trenders_google:latest
