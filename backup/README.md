# Backup

Simple `rsync` script that backups the directories configured in `sync_config.conf`.

If the config file was changed using Windows, run `dos2unix sync_config.conf`

## Cron Job

Open crontab as root `sudo crontab -e` and add the following lines

```
# Run backup script on Mondays and Thursdays
0 0 * * 1,4 /home/florin/homelab/backup/backup.sh

# Run backup script at system startup
@reboot /home/florin/homelab/backup/backup.sh
``` 

Or run `make run` to take on-demand backups
