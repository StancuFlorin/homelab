# Bitwarden

## Docs

- [https://bitwarden.com/help/install-on-premise-manual/](https://bitwarden.com/help/install-on-premise-manual/)

## Settings

- Copy `config.json.example` to `config.json` and update it with your data.  
  - The `SMTP` details are required to fully use Bitwarden. You can get a free SMTP server from https://app.brevo.com/settings/keys/smtp
  - Get a Bitwarden installation key from https://bitwarden.com/host/
  - I personally recomand [nginx-proxy-manager](../nginx-proxy-manager/) to have a nice local URL like https://bitwarden.home.stancu.me without any SSL issues
- run `make install`
- run `make run`

### Published Ports

http: 87  
https: 447
