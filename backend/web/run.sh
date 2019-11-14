#!/bin/sh
set -e
docker pull antoninagerasiova/trenders_mixer:latest
docker run --network host -e DATABASE_URL=postgresql://me:hackme@127.0.0.1/trends -it --rm antoninagerasiova/trenders_mixer:latest

