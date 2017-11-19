#!/bin/bash

set -e -u

sed -i 's/#\(en_US\.UTF-8\)/\1/' /etc/locale.gen
locale-gen

ln -sf /usr/share/zoneinfo/UTC /etc/localtime

usermod -s /usr/bin/zsh root
cp -aT /etc/skel/ /root/
chmod 700 /root

sed -i 's/#\(PermitRootLogin \).\+/\1yes/' /etc/ssh/sshd_config
sed -i "s/#Server/Server/g" /etc/pacman.d/mirrorlist
sed -i 's/#\(Storage=\)auto/\1volatile/' /etc/systemd/journald.conf

sed -i 's/#\(HandleSuspendKey=\)suspend/\1ignore/' /etc/systemd/logind.conf
sed -i 's/#\(HandleHibernateKey=\)hibernate/\1ignore/' /etc/systemd/logind.conf
sed -i 's/#\(HandleLidSwitch=\)suspend/\1ignore/' /etc/systemd/logind.conf

(crontab -l 2>/dev/null; echo "@reboot sh /root/networking.sh") | crontab -

systemctl enable pacman-init.service choose-mirror.service
systemctl set-default multi-user.target
systemctl enable cronie.service
systemctl disable netctl.service

cd /
git clone https://github.com/smcameron/space-nerds-in-space.git 
git clone https://github.com/smcameron/space-nerds-in-space-assets.git 
cp -R space-nerds-in-space-assets/share/snis/solarsystems/* space-nerds-in-space/share/snis/solarsystems/
cd space-nerds-in-space
make
cd ..
rm -rf space-nerds-in-space-assets

git clone https://github.com/cmusphinx/sphinxbase.git
cd sphinxbase
sh ./autogen.sh
sh ./configure --enable-fixed
make
make install
cd ..

git clone https://github.com/cmusphinx/pocketsphinx.git
cd pocketsphinx
sh ./autogen.sh
sh ./configure
make
make install
cd ..
