# Bitwarden

## Overview
This guide provides instructions for setting up Bitwarden, an open-source password management solution. By following these steps, you'll be able to deploy Bitwarden on your own premises, ensuring greater control over your password management system.

## Documentation
For detailed instructions and additional help, refer to the official Bitwarden documentation: [Bitwarden Installation Guide](https://bitwarden.com/help/install-on-premise-manual/).

## Setup
1. Copy `config.json.example` to `config.json` and update it with your configuration details.  
  1.1. SMTP details are required for full functionality. Obtain a free SMTP server from [Brevo SMTP](https://app.brevo.com/settings/keys/smtp).  
  1.2. Get a Bitwarden installation key from [Bitwarden](https://bitwarden.com/host/).
2. For a smoother experience, it's recommended to use [nginx-proxy-manager](../nginx-proxy-manager) to manage local URLs like https://bitwarden.home.stancu.me without SSL issues.
3. Run `make install` to install Bitwarden.
4. Run `make run` to start Bitwarden.

## Settings
If any changes are made to `config.json`, execute `make restart` to update the .env files and restart the containers.

## Published Ports
The following ports are published:

- HTTP: 87
- HTTPS: 447

## Note
- Regularly update Bitwarden and its dependencies to ensure security and stability.
- Back up your configuration files and data regularly to prevent data loss. Check my [backup](../backup) script to see how I do it.
- For any issues or inquiries, consult the official documentation or reach out to Bitwarden support.
