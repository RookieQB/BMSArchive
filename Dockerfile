FROM nginx:1.27-alpine

# Remove the default nginx config
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html    /usr/share/nginx/html/index.html
COPY database.html /usr/share/nginx/html/database.html
COPY data.json     /usr/share/nginx/html/data.json

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
