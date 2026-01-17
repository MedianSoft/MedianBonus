FROM node:20-alpine

RUN apk add --no-cache python3 make g++ bash

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY tsconfig.json ./

COPY . .

ENV NODE_ENV=development
ENV REACT_APP_APP_NAME="Code Battle"
ENV REACT_APP_AUTH_DELAY_MS=600
ENV PORT=3000
ENV CHOKIDAR_USEPOLLING=true
ENV WATCHPACK_POLLING=true
ENV FAST_REFRESH=true

EXPOSE 5173

CMD ["npm", "run", "dev"]