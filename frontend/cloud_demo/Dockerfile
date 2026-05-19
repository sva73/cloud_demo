# Build Stage
FROM node:22 AS build

WORKDIR /cloud_demo

COPY package*.json ./

RUN npm install

COPY . .

RUN npm run build

# Runtime Stage
FROM nginx:stable-alpine

COPY --from=build /could_demo/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]