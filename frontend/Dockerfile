# frontend/Dockerfile
#FROM nginx:alpine
#COPY nginx.conf /etc/nginx/nginx.conf
#COPY index.html /usr/share/nginx/html/cicd/frontend/index.html

FROM nginx:alpine

# Poista oletussivu
RUN rm -rf /usr/share/nginx/html/*

# Kopioi frontend
COPY index.html /usr/share/nginx/html/index.html

# Kopioi nginx-konfiguraatio
COPY nginx.conf /etc/nginx/conf.d/default.conf
