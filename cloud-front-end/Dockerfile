FROM node

WORKDIR /client

COPY package.json .

RUN npm i

COPY . .

CMD ["npm", "start", "0.0.0.0:3000"]
