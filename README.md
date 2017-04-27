# snis-live
A bootable live image based of Arch Linux customised to run the game Space Nerds In Space by smcameron.
https://github.com/smcameron/space-nerds-in-space

## Requirements (for building from source)
archiso
git
base-devel

## Building
###### NOTE: Building the ISO requires an x86_64 pc running Arch Linux.
To build from source, run the `./autobuild` script as root (because of permissions around files used by [archiso](https://wiki.archlinux.org/index.php/Archiso#Setup)). The script will clone and build space nerds in space, then build the ISO. Once it has completed, an ISO file will have be created in the `/out` directory.
