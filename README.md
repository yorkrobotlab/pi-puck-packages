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


## Building Packages

Packages in this repository can be built into debs using the `debuild` tool.
Enter each package directory and run:
```
debuild -i -us -uc -b
```


### Creating/Hosting a Repository

There are many ways to create and publish a Debian package repository, including just manually constructing files and folders in the correct format.

One convenient option for managing small repositories like this is [aptly](https://www.aptly.info).
The process we use for publishing packages through aptly looks something like the following.

First create and export a GPG key pair for signing the repository:
```
gpg --full-generate-key
gpg --export-secret-keys --armor user@domain.com > pi-puck-repo-privkey.asc
gpg --export --armor user@domain.com > pi-puck-repo-pubkey.asc
gpg --output pi-puck-repo-revoke.asc --gen-revoke user@domain.com
```

The private key should be kept safe and will be used to sign packages in the repository, while the public key will need to be distributed to users and installed in apt on the Raspberry Pis.

First run `aptly config show` to create a default configuration file at `~/.aptly.conf`.

Next, add a [`FileSystemPublishEndpoints` entry](https://www.aptly.info/doc/feature/filesystem/) like the following for the Pi-puck repository in the aptly configuration file.
```
"FileSystemPublishEndpoints": {
  "pi-puck": {
    "rootDir": "/path/to/pi-puck/repository",
    "linkMethod": "copy",
    "verifyMethod": "md5"
  }
}
```

Then create a new repository and add the debs:
```
aptly repo create -comment="Pi-puck supporting packages" pi-puck
mkdir debs
cp pi-puck-packages/*.deb debs
aptly repo add pi-puck debs
```

To create a snapshot of the repository and publish a signed copy to the directory specified in the config file, run the following (using whatever unique `VERSION` number you like):
```
export VERSION=20200519-1
aptly snapshot create pi-puck_$VERSION from repo pi-puck
aptly publish snapshot -distribution=buster pi-puck_$VERSION filesystem:pi-puck:debian
```

Ensure that the published repository has been signed with the correct PGP key.

Finally, serve the contents of the output folder on a web server and set it as a package repository in Raspbian.

In future, to update the repository with a new snapshot of the packages, set a new `VERSION` number and run:
```
cp pi-puck-packages/*.deb debs
aptly repo add pi-puck debs
export VERSION=20200519-2
aptly snapshot create pi-puck_$VERSION from repo pi-puck
aptly publish switch buster filesystem:pi-puck:debian pi-puck_$VERSION
```


## Licence

Unless otherwise specified, software is licensed under an [MIT Licence][mit].

[mit]: /LICENSE
