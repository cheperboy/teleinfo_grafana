# influx

## create database and user

``` bash
create database teleinfo
create user grafana with password xxx with all privileges
grant all privileges on teleinfo to grafana
```

## usefull commands

``` bash
show users
show DATABASES
USE teleinfo
SHOW SERIES
SHOW MEASUREMENTS
SELECT * FROM "BASE" LIMIT 5
exit
```

# Supervisor

file `/etc/supervisor/conf.d/teleinfo.conf`
``` bash
[program:teleinfo]
user=pi
command = python /home/pi/teleinfo/teleinfo.py
directory =      /home/pi/teleinfo/
stdout_logfile = /home/pi/teleinfo/log/teleinfo.log
stderr_logfile = /home/pi/teleinfo/log/teleinfo_err.log
stdout_logfile_maxbytes=4MB
stdout_logfile_backups=4
stderr_logfile_maxbytes=4MB
stderr_logfile_backups=4
autostart=true
autorestart=true
```
