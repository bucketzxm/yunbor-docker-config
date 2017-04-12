echo 'yunbor' |sudo sed -i 's/mirrors.163.com/mirrors.ustc.edu.cn/g' /etc/apt/sources.list


# update apt source to shuosc's mirror
sudo apt-get update -y
sudo apt-get upgrade -y

sudo apt-get install ssh -y
# install docker
sudo apt-get install apt-transport-https ca-certificates curl software-properties-common -y
curl -fsSL https://download.docker.com/linux/debian/gpg | sudo apt-key add -
sudo apt-key fingerprint 0EBFCD88
sudo add-apt-repository "deb [arch=amd64] https://download.docker.com/linux/debian $(lsb_release -cs) stable"

sudo apt-get update
sudo apt-get install docker-ce -y


sudo apt-get install make -y

# set init to terminal mode
sudo rm /etc/systemd/system/default.target
sudo ln -s /lib/systemd/system/multi-user.target /etc/systemd/system/default.target

# add current user to docker group
sudo usermod -aG docker yunbor

sudo reboot
