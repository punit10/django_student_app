# django_student_app
This is django basic app please follow the below setup to deploy on aws EC2

**VS Code Setup (if running on local machine)**

Windows Ctrl shift P then select interpreter

Python —version

Pip3 –version

python.exe -m pip install --upgrade pip

pip3 install pipenv

pipenv install django

pipenv shell

python -c "import os, sys; print(os.path.dirname(sys.executable))"

**EC2 Instance Setup** 

On ec2 Linux root

After connecting

One time setup>> (Optionally you can work with ubuntu user, then no need to add user) 

adduser punit

usermod -aG sudo punit

su - punit

python -V

sudo apt-get update

sudo apt-get upgrade

python3 -V

sudo apt-get install python3-venv

python3 -m venv djangoEnv

source djangoEnv/bin/activate

Every time After connecting to ec2>>

su - punit

source djangoEnv/bin/activate

**Setting up Nginx and gunicorn**

python3 -m venv djangoEnv

source djangoEnv/bin/activate

pip3 install django

git clone https://github.com/punit10/django_student_app.git student

mv django_student_app/ student

"add the IP address to setting.py allowed hosts" 

sudo apt-get install -y nginx

pip install gunicorn

sudo apt-get install supervisor

cd /etc/supervisor/conf.d/

sudo touch gunicorn.conf

sudo chmod 707 gunicorn.conf

vi gunicorn.conf

<paste below code>
  
[program:gunicorn]

directory=/home/ubuntu/student

command=/home/ubuntu/djangoEnv/bin/gunicorn --workers 3 --bind unix:/home/ubuntu/student/app.sock student.wsgi:application  
autostart=true
autorestart=true
stderr_logfile=/var/log/gunicorn/gunicorn.err.log
stdout_logfile=/var/log/gunicorn/gunicorn.out.log

[group:guni]

programs:gunicorn
<code end>

sudo mkdir /var/log/gunicorn

sudo supervisorctl reread

OUTPUT>>>
guni: available

sudo supervisorctl update

OUTPUT>>>
guni: added process group

sudo supervisorctl status

OUTPUT<<should be running>>

cd /etc/nginx/

sudo touch nginx.conf

sudo chmod 707 nginx.conf

vi nginx.conf

"# change user to root"
  
sudo touch django.conf

sudo chmod 707 django.conf

vi django.conf

<paste code change server name>

#### Code starts  
server{
	listen 80;
	server_name <<ec2 public IP>>;
 
	location / {
		include proxy_params;
		proxy_pass http://unix:/home/ubuntu/student/app.sock;
	}
}
#### Code ends

sudo nginx -t

OUTPUT>>
nginx: the configuration file /etc/nginx/nginx.conf syntax is ok
nginx: configuration file /etc/nginx/nginx.conf test is successful

sudo ln django.conf /etc/nginx/sites-enabled

sudo service nginx restart
