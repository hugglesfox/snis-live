#!/bin/bash

hostname $((1 + RANDOM % 1000))
systemctl start netctl.service
systemctl start netctl-ifplugd@$((ls -1 /sys/class/net | head -1))
