#This file os never gonna be use this is to store config template
[program:gunicorn]
directory=/home/ubuntu/student
command=/home/ubuntu/djangoEnv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/student/app.sock student.wsgi:application  
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log

[group:guni]
programs:gunicorn


#config for ngnix
server{
	listen 80;
	server_name <Ec2 IP> ;
    
	location / {
		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/student/app.sock;
	}
}
