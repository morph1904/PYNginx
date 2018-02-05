# PYNginx
A Django based Nginx control panel with SSH and Reverse Proxy

## Install
I will try to script this up at some point. 
### Install pip
    sudo apt install python-pip -y
### Install virtualenv
    sudo pip install virtualenv

### Create directories 
    mkdir /app
    cd /app
    
### Create and setup virtualenv
    virtualenv pynginx
    source pynginx/bin/activate
    
### Clone PYNginx
    git clone https://github.com/morph1904/PYNginx.git
    cd PYNginx/src
    
### Install app server
    pip install uwsgi
    
### Install app dependencies    
    pip install -r requirements.txt
    
### Remove Apache and Install NGINX
    service apache2 stop
    sudo apt remove apache2
    sudo apt install nginx -y
    sudo ufw allow 'Nginx Full'
    
### Edit file uwsgi.ini to match system
    nano /app/PYNginx/src/uwsgi.ini
    
### Edit IP Address and port for the app to run on
    #Edit this for your server
    http = 192.168.1.194:8000
    
### Apply correct permissions and set owner
    sudo chown -R nobody:nogroup /app/PYNginx 
    sudo chmod -R 0777 /app/PYNginx 
    
### Create app service
    sudo nano /etc/init/uwsgi.conf
    
    [Unit]
    Description=uWSGI
    Wants=network.target
    After=network.target

    [Service]
    WorkingDirectory=/app/PYNginx/src
    Environment="PATH=/app/pynginx/bin"
    ExecStart=/app/pynginx/bin/uwsgi --ini /app/PYNginx/src/uwsgi.ini

    # Requires systemd version 211 or newer
    RuntimeDirectory=uwsgi
    Restart=always
    KillSignal=SIGQUIT
    Type=notify
    StandardError=syslog
    NotifyAccess=all

    [Install]
    WantedBy=multi-user.target
    
###Activate service on boot
    sudo systemctl activate uwsgi.service