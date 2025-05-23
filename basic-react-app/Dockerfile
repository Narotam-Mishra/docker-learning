FROM node:22-slim

WORKDIR /myapp

COPY . . 

RUN npm install

EXPOSE 5168

CMD [ "npm", "run", "dev" ]