#!/usr/bin/env python
from control import x


def ubuntu_update():
    x("apt update")
    x("apt upgrade;  snap refresh")
    x("pip3 install --upgradepip; clear")