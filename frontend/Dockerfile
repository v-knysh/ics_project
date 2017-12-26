FROM node
WORKDIR /frontend
ADD . /frontend

RUN npm install
#RUN npm run dev

EXPOSE 8080

CMD ["npm", "run", "dev", "-a 0.0.0.0", "-p 8080"]

