FROM node:8

ENV appdir /app
COPY / $appdir
WORKDIR $appdir
RUN npm ci
RUN npm run deploy

ARG NODE_ENV

ENV PORT="80" \
    TZ=Europe/Moscow \
    NODE_ENV=${NODE_ENV}

CMD npm start
