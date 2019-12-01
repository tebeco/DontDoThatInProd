FROM node:12.13.1-alpine3.10 AS build
WORKDIR /app

COPY ./package.json .
COPY ./package-lock.json .
RUN npm ci

FROM node:12.13.1-alpine3.10 AS runtime
WORKDIR /app
COPY --from=build /app/node_modules/ ./node_modules/
COPY ./src/ ./src/

EXPOSE 3000

CMD ["node", "./src/app.js"]