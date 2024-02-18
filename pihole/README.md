# Pi-Hole

Network-wide Ad Blocking

## Docs

- [https://github.com/pi-hole/docker-pi-hole](https://github.com/pi-hole/docker-pi-hole)
- [https://docs.pi-hole.net/main/post-install/](https://docs.pi-hole.net/main/post-install/)

## Settings

### Default Credentials

```
sudo docker logs pihole | grep random
```

### Published Ports

http: 82    
tcp / udp: 53  
udp: 67

port `53` is probably used by `systemd-resolved` service and you need to disable it

```
sudo systemctl disable systemd-resolved.service
sudo systemctl stop systemd-resolved

sudo sh -c 'echo "nameserver 8.8.8.8" >> /etc/resolv.conf'
```