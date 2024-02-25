# Backup Script

## Overview
This project provides a simple yet effective solution for automating backups using rsync. The script, configured through `sync_config.conf`, facilitates the backup of specified directories, ensuring data safety and integrity.

# Setup

1. Ensure `sync_config.conf` is appropriately configured. If changes are made on Windows, execute `dos2unix sync_config.conf` to ensure compatibility.
2. Set up Cron Job to automate backups:
  2.1 Open crontab as root using sudo crontab -e.
  2.2 Add the following lines:
   
```
# Run backup script on Mondays and Thursdays
0 0 * * 1,4 /home/florin/homelab/backup/backup.sh

# Run backup script at system startup
@reboot /home/florin/homelab/backup/backup.sh
```

3. Alternatively, you can trigger backups on-demand by running `make run`.

# Usage
Execute the provided script `backup.sh` to initiate backups based on the configured settings in `sync_config.conf`. Ensure proper permissions are set to execute the script.

# Note
- It's crucial to review and update `sync_config.conf` whenever directories or backup requirements change.
- Regularly monitor backup logs and outputs to ensure backups are running smoothly and effectively. Check my [nginx](../nginx) and [homepage](../homepage) docker containers to see how I do it.
  
![widget](../homepage/pics/backup_widget.png)
