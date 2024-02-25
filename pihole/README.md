# Pi-Hole: Network-wide Ad Blocking

## Overview
Pi-Hole is a network-wide ad blocker that works at the DNS level, providing ad blocking for all devices on your network. It efficiently blocks advertisements, trackers, and malicious domains, enhancing your browsing experience and network security.

## Documentation
For detailed instructions and post-installation setup, refer to the Pi-Hole documentation:

- [Pi-Hole Docker GitHub Repository](https://github.com/pi-hole/docker-pi-hole)
- [Pi-Hole Post-Installation Guide](https://docs.pi-hole.net/main/post-install/)

## Setup

- Start Pi-Hole with a simple command: `make run`.
- Change your router's `WAN DNS settings` to point to the local IP address where Pi-Hole is running.

## Settings

### Default Credentials
Retrieve the default password using the following command:
```
sudo docker logs pihole | grep random
```

### Published Ports
The following ports are accessible:

- HTTP: 82
- TCP/UDP: 53
- UDP: 67

Note: Port 53 might be occupied by the `systemd-resolved` service. Disable and stop the service before running Pi-Hole:
```
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved
```

Additionally, append a DNS nameserver to `/etc/resolv.conf`:
```
sudo sh -c 'echo "nameserver 8.8.8.8" >> /etc/resolv.conf'
```
