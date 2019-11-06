FROM node:12

ENV appdir /client
COPY / $appdir
WORKDIR $appdir
RUN npm ci --only=production
RUN npm run deploy

ARG NODE_ENV

ENV PORT="80" \
    TZ=Europe/Moscow \
    NODE_ENV=${NODE_ENV}

CMD npm start
