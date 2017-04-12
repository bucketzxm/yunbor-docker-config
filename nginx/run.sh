docker run --name mynginx -v /data/SHU/finalProject/museum/docker/nginx/data:/usr/share/nginx/html:ro -v /data/SHU/finalProject/museum/docker/nginx/config:/etc/nginx:ro -p 80:80 -p 443:443 -d nginx
