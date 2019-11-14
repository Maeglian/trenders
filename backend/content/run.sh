#!/bin/sh
set -e
docker pull antoninagerasiova/trenders_efir:latest
docker run -p8081:8080 -it --rm antoninagerasiova/trenders_efir:latest

