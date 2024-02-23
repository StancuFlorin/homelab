# Nginx Proxy Manager

Expose your services easily and securely

## Docs

- [https://nginxproxymanager.com/guide/](https://nginxproxymanager.com/guide/)
- [https://github.com/NginxProxyManager/nginx-proxy-manager](https://github.com/NginxProxyManager/nginx-proxy-manager)

## Setup

You will need a paid domain name (subdomain is also good) or even a free one (more details [here](https://www.getfreedomain.name)).

Setup the domain name with Cloudflare and add the following DNS records to point to your local network (change the IP with the one used by your homeLAB).

You will use the public DNS servers to translate my-service.home.stancu.me to your private address. To access `my-service` you will need to login into [nginx-proxy-manager](http://192.168.50.133:81) and add your proxy hosts there.

Use `make run` to start the `nginx-proxy-manager` service.

Before ading any proxy hosts, you will need to configure a SSL certificate. nginx-proxy-manager has a direct integration with Cloudflare and you can generate one easily.

### Cloudflare DNS

```
A   home.stancu.me      192.168.50.133      DNS only - reserved IP
A   *.home.stancu.me    192.168.50.133      DNS only - reserved IP
```

## Settings

### Default Credentials

username: admin@example.com  
password: changeme

### Published Ports

http: 80 (don't change it for an easy integration with Cloudflare)  
http: 81  
https: 443
