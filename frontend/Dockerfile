FROM node:20-alpine

RUN apk add --no-cache python3 make g++ bash

WORKDIR /app

COPY package*.json ./

RUN npm install

COPY tsconfig.json ./

COPY . .

EXPOSE 5173

CMD ["npm", "run", "dev", "--host"]