# Make sure to run the container with --privileged
# Needs a volume mounted to /snis-live/out/
#
# build example
#   docker build -t snis-live .
#
# command example:
#   docker run --privileged -v $HOME/snislive-docker/:/snis-live/out/ snis-live
#

FROM base/archlinux

WORKDIR /snis-live

RUN pacman -Sy --noconfirm \
    git \
    archiso \
    base-devel

ADD ./airootfs /snis-live/airootfs
ADD ./efiboot /snis-live/efiboot
ADD ./isolinux /snis-live/isolinux
ADD ./syslinux /snis-live/syslinux
ADD ./autobuild /snis-live/autobuild
ADD ./build.sh /snis-live
ADD ./mkinitcpio.conf /snis-live
ADD ./packages.x86_64 /snis-live
ADD ./pacman.conf /snis-live

CMD sh ./autobuild
