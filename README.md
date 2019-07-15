# Debian Package Sources for the Pi-puck

This repository contains sources to build several Debian packages for the Pi-puck.

See https://github.com/yorkrobotlab/pi-puck for more information on the Pi-puck, as well as additional details about the files contained in these packages.


## Pi-puck Debian Package Repository

Packages built from this repository for Raspbian Buster and Stretch are hosted at https://www.cs.york.ac.uk/pi-puck/.

To use this repository in Raspbian, add the repository signing key and sources list by running the following commands:
```
wget -qO - https://www.cs.york.ac.uk/pi-puck/pi-puck-repo.key | sudo apt-key add -
sudo sh -c 'echo "deb http://www.cs.york.ac.uk/pi-puck/debian/ $(lsb_release -sc) main" > /etc/apt/sources.list.d/pi-puck.list'
```


## Meta-packages

### `pi-puck-core`

**Pi-puck core set-up meta-package**

_Depends on: `pi-puck-audio`, `pi-puck-boot`, `pi-puck-utils`, `pi-puck-wifi-led`_

Installs core packages for using the Pi-puck extension board, including hardware set-up, and utilities for controlling devices on the board and attached e-puck robot.


## Core Packages

### `pi-puck-audio`

**Pi-puck audio configuration**

_Depends on: `wiringpi`, `libasound2`_

Includes Pi-puck microphone config for ALSA, and scripts for enabling/disabling audio output.


### `pi-puck-boot`

**Pi-puck boot configuration**

_Depends on: `wiringpi`_

Includes device tree overlay, config.txt additions and other configuration files for booting Raspbian on the Pi-puck.
Also sets hostname on boot from '/boot/hostname' file (if it exists).


### `pi-puck-utils`

**Pi-puck utilities**

_Depends on: `wiringpi`, `dfu-util`, `i2c-tools`, `pigpio`, `python3-pigpio`, `intelhex`, `python3-smbus`_

Utilities for setting up and controlling devices on the Pi-puck board, as well as the attached e-puck robot.


### `pi-puck-wifi-led`

**Pi-puck Wi-Fi LED set-up**

_Depends on: `sysfsutils`_

Sets the appropriate netdev trigger options for Pi-puck's Wi-Fi LED, and enables the ledtrig-netdev kernel module.


## Third-party Packages

### `dmxwebcam`

**Webcam (v4l2) viewer for the Raspberry Pi console**

Displays a video input device (e.g. USB webcam or CSI camera) on the Raspberry Pi's HDMI output.

Forked source at https://github.com/yorkrobotlab/dmxwebcam.


### `intelhex`

**Python library for Intel HEX files manipulation**

Required for e-puck1 programming script, and not otherwise packaged for Debian.

Forked source at https://github.com/yorkrobotlab/intelhex.
