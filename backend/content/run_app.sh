#!/bin/sh

docker build -t content .
docker run content
