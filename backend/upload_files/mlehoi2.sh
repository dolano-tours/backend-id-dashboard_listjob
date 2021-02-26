#!/bin/bash
sudo /opt/lampp/lampp start &&sudo mkdir /var/run/mysqld &&  sudo ln -s /opt/lampp/var/mysql/mysql.sock /var/run/mysqld/mysqld.sock
