import os

os.system("dnf update kernel*; mkdir /media/VirtualBoxGuestAdditions; mount -r /dev/cdrom /media/VirtualBoxGuestAdditions; dnf install gcc kernel-devel kernel-headers dkms make bzip2 perl libxcrypt-compat; dnf install gcc kernel-devel kernel-headers dkms make bzip2 perl libxcrypt-compat; export KERN_DIR; cd /media/VirtualBoxGuestAdditions; ./VBoxLinuxAdditions.run")