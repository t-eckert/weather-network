FROM node:17-alpine as build

WORKDIR /var/www/frontend
COPY . /var/www/frontend
RUN npm ci
RUN npm run build

FROM node:17-alpine as run

WORKDIR /var/www/frontend
COPY --from=build /var/www/frontend .
COPY . .

EXPOSE 3000
CMD ["node", "./dist"]