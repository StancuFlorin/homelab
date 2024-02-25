# Speedtest Tracker: Self-Hosted Internet Performance Tracker

## Overview
Speedtest Tracker is a self-hosted application designed for tracking internet performance. It conducts periodic speedtest checks against Ookla's Speedtest service, allowing users to monitor their internet connection's speed and reliability.

## Documentation
For detailed instructions and usage guidelines, refer to the Speedtest Tracker documentation:

- [Speedtest Tracker Documentation](https://docs.speedtest-tracker.dev/)
- [Speedtest Tracker GitHub Repository](https://github.com/alexjustesen/speedtest-tracker)

## Setup

Initiate Speedtest Tracker with a simple command: `make run`.

## Settings

Configure the speedtest schedule (using the web admin console) using cron syntax. For example, to run speedtest checks every 2 hours, use:
```
0 */2 * * *
```

### Default Credentials

- Username: admin@example.com
- Password: password
  
### Published Ports
The following ports are accessible:

- HTTP: 8080
- HTTPS: 8443
 
## Note
- Speedtest Tracker provides a convenient solution for tracking internet performance metrics over time.
- Customize the speedtest schedule and adjust settings according to your preferences and requirements.
- For any issues or inquiries, consult the documentation or community support resources.
