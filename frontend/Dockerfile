FROM node:22.7.0

ARG FRNT_WORKDIR
ARG FRNT_PORT

WORKDIR ${FRNT_WORKDIR}

COPY package*.json ./

RUN npm install

RUN npm install -g @ionic/cli cordova

COPY . .

EXPOSE ${FRNT_PORT}