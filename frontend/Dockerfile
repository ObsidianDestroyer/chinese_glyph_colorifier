# Build stage
FROM node:lts-alpine as build-stage

WORKDIR /usr/src/app
ENV PATH /app/node_modules/.bin:$PATH
COPY package.json /usr/src/app/package.json
RUN npm install --silent

COPY . /usr/src/app
RUN npm run build


# Production stage
FROM nginx:stable-alpine as build-nginx

COPY --from=build-stage /usr/src/app/dist /usr/share/nginx/html
RUN rm /etc/nginx/conf.d/default.conf

WORKDIR /etc/nginx

CMD ["nginx", "-g", "daemon off;"]
