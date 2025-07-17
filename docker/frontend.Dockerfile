# Build step
FROM node:18 AS builder

WORKDIR /app

COPY frontend/ .

RUN npm install
RUN npm run build

# Serve build with Nginx
FROM nginx:alpine

COPY --from=builder /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
