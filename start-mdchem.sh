#!/bin/bash
# Starts the MDChem

echo "clearing apache error log"
rm -rf /var/log/apache2/*

echo "restarting apache2 server"
service apache2 reload

echo "restarting mysql daemon"
service mysql restart
