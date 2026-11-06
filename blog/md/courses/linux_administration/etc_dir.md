# /etc dir

Here's a table summarizing the most important configuration files in the `/etc/` directory:

| **File**                       | **Purpose**                                                                 |
|---------------------------------|-----------------------------------------------------------------------------|
| `/etc/passwd` | Stores user account information. |
| `/etc/shadow` | Stores encrypted passwords. |
| `/etc/group` | Stores group information. |
| `/etc/gshadow` | Stores secure group data. |                                 |
| `/etc/fstab`                    | Lists filesystems and partitions to be mounted at boot time.                 |
| `/etc/network/interfaces` (or `/etc/netplan/`) | Configures network interfaces (IP, subnet, gateway).                |
| `/etc/hostname`                 | Contains the system's hostname (machine name on the network).               |
| `/etc/hosts`                    | Maps IP addresses to hostnames for local resolution.                         |
| `/etc/sudoers`                  | Configures user and group permissions for `sudo` command access.            |
| `/etc/ssh/sshd_config`          | Configures SSH server settings (authentication, ports, access).            |
| `/etc/cron.d/`, `/etc/crontab`, `/etc/cron.daily/` | Defines scheduled tasks (cron jobs).                           |
| `/etc/sysctl.conf`              | Configures kernel parameters for system tuning (e.g., memory, networking).  |
| `/etc/resolv.conf`              | Specifies DNS servers for domain name resolution.                           |
| `/etc/pam.d/`                   | Contains PAM configuration files for system authentication.                |
| `/etc/systemd/system/`          | Defines systemd unit configuration files for services and other system components. |
| `/etc/logrotate.conf` and `/etc/logrotate.d/` | Configures log file rotation.                                          |

This table should give you a quick reference to these crucial configuration files and their purposes.