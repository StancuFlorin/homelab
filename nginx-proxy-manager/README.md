# Nginx Proxy Manager: Simplified Service Exposure

## Overview
Nginx Proxy Manager offers a convenient and secure way to expose your services to the internet. By utilizing this tool, you can easily manage proxy hosts, set up SSL certificates, and ensure secure access to your services.

## Documentation
Refer to the Nginx Proxy Manager documentation for detailed guides and instructions:

- [Nginx Proxy Manager Guide](https://nginxproxymanager.com/guide/)
- [Nginx Proxy Manager GitHub Repository](https://github.com/NginxProxyManager/nginx-proxy-manager)

## Setup

- Domain Name Setup:  
  - Obtain a domain name, which can be a paid domain or a free one.  
  - Configure your domain with Cloudflare and add the following DNS records to point to your local network, replacing the IP address with your homeLAB's IP.
```
A   home.stancu.me      192.168.50.133      DNS only - reserved IP
A   *.home.stancu.me    192.168.50.133      DNS only - reserved IP
```

- Start Nginx Proxy Manager:  
  - Execute `make run` to start the nginx-proxy-manager service.
   
- SSL Certificate Configuration:  
  - Before adding any proxy hosts, configure an SSL certificate. Nginx Proxy Manager offers direct integration with Cloudflare, simplifying the process of generating SSL certificates.

## Settings
### Default Credentials
- Username: admin@example.com
- Password: changeme

### Published Ports
The following ports are published:

- HTTP: 80 (for easy integration with Cloudflare)
- HTTP: 81
- HTTPS: 443
  
## Note
- Nginx Proxy Manager simplifies the process of managing proxy hosts and SSL certificates, ensuring secure access to your services.
- Make sure to change the default credentials after initial setup to enhance security.
- For assistance or further information, consult the documentation or community support resources.
