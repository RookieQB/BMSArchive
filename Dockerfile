FROM nginx:1.27-alpine

# Remove the default nginx config
RUN rm /etc/nginx/conf.d/default.conf

COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY index.html    /usr/share/nginx/html/index.html
COPY checkout-success.html /usr/share/nginx/html/checkout-success.html
COPY database.html /usr/share/nginx/html/database.html
COPY grow.html     /usr/share/nginx/html/grow.html
COPY data.json     /usr/share/nginx/html/data.json
COPY tailwind.js   /usr/share/nginx/html/tailwind.js
COPY robots.txt    /usr/share/nginx/html/robots.txt
COPY sitemap.xml   /usr/share/nginx/html/sitemap.xml
COPY og-image.png  /usr/share/nginx/html/og-image.png
COPY favicon.svg   /usr/share/nginx/html/favicon.svg

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
