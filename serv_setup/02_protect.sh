#!/bin/bash 

apt install fail2ban -y && systemctl start fail2ban && systemctl enable fail2ban
add user user123 
# enter password
# can skip additional data (y)

# Add the user to sudo group 
usermod -aG sudo user123
su - user123
