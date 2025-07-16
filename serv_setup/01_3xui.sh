#!/bin/bash 

# Connect 
# ssh root@ip_address
apt update && apt upgrade -y

# install python
apt install curl -y 

bash <(curl -Ls https://raw.githubusercontent.com/mhsanaei/3x-ui/master/install.sh)

# Continue w/ mods?: Y
# Username, Pwd? bash <(curl -Ls https://raw.githubuswercont)
set port 5666
