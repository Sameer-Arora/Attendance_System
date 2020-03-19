#!/bin/bash

sudo -i 
apt update
apt install nginx
ufw app list
ufw allow 'Nginx HTTP'
ufw enable
ufw status
systemctl status nginx
