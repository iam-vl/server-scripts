#!/bin/bash 


apt-get install gawk bison gcc make wget tar -y
wget -c https://ftp.gnu.org/gnu/glibc/glibc-2.35.tar.gz
tar -zxvf glibc-2.35.tar.gz && cd glibc-2.35
ls
../configure --prefix=/opt/glibc
make
make install