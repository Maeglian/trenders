#!/bin/sh
set -e
docker build . -t antoninagerasiova/trenders_efir:latest
docker push antoninagerasiova/trenders_efir:latest
