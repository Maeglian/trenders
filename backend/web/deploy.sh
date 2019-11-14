#!/bin/sh
set -e
docker build . -t antoninagerasiova/trenders_mixer:latest
docker push antoninagerasiova/trenders_mixer:latest
