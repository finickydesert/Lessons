#!/usr/bin/env python
import os
from ubuntu_sys_update import ubuntu_update
from control import x
from installing_apps import apps

#system matinance that are needed 
x("apt purge firefox")
x("apt remove --purge libreoffice*")

ubuntu_update()
apps()

#random things to be done
#why get nodic, because I can.
x("git clone https://github.com/EliverLara/Nordic.git")
x("mv Nordic/ ~/.themes/")
x("reboot")