#!/bin/bash 

apt install fail2ban -y && systemctl start fail2ban && systemctl enable fail2ban
add user user123 
# enter password
# can skip additional data (y)

# Add the user to sudo group 
usermod -aG sudo user123
su - user123 


# To block root access thru ssh: 
# sudo nano /etc/ssh/sshd_config 
# Change val: Permit root login: no 

# apply the configs  
# sudo service sshd restart 



