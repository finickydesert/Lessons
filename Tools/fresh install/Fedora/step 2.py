import os

os.system("sudo dnf install https://download1.rpmfusion.org/free/fedora/rpmfusion-free-release-$(rpm -E %fedora).noarch.rpm https://download1.rpmfusion.org/nonfree/fedora/rpmfusion-nonfree-release-$(rpm -E %fedora).noarch.rpm;
os.system("sudo wget https://downloads.nordcdn.com/configs/archives/servers/ovpn.zip")
os.system("sudo rpm --import https://packages.microsoft.com/keys/microsoft.asc; curl https://packages.microsoft.com/config/rhel/7/prod.repo | sudo tee /etc/yum.repos.d/microsoft.repo")
os.system("sudo dnf update -y; sudo dnf install youtube-dl p7zip p7zip-plugins p7zip-gui -y")
os.system("sudo dnf install openvpn golang ruby wget -y")
os.system("sudo  flatpak install flathub org.videolan.VLC -y")
os.system("sudo flatpak install flathub com.discordapp.Discord -y; sudo flatpak install flathub org.vim.Vim -y")
os.system("sudo flatpak install flathub com.valvesoftware.Steam -y; sudo gem install lolcat")
os.system("sudo dnf install fortune-mod cowsay -y; sudo flatpak install org.libreoffice.LibreOffice -y")
os.system("sudo flatpak install com.visualstudio.code -y; sudo flatpak install flathub org.wireshark.Wireshark -y")
os.system("sudo dnf install akmod-wl ca-certificates unzip -y; sudo dnf update -y; sudo dnf install compat-openssl10 -y")
os.system("sudo dnf install -y powershell dwm dwm-user")
os.system("sudo shutdown -r 0")