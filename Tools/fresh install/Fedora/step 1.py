import os

os.system("flatpak remote-add --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo")
os.system("sudo dnf update kernel*")
os.system("mkdir /media/VirtualBoxGuestAdditions")
os.system("mount -r /dev/cdrom /media/VirtualBoxGuestAdditions")
os.system("sudo dnf install gcc kernel-devel kernel-headers dkms make bzip2 perl libxcrypt-compat")
os.system("dnf install gcc kernel-devel kernel-headers dkms make bzip2 perl libxcrypt-compat")
os.system("export KERN_DIR; cd /media/VirtualBoxGuestAdditions; ./VBoxLinuxAdditions.run")
