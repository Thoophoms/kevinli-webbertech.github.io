# Linux Ref

## help commands

* `compgen`

`compgen -c` will list all the commands you could run.

`compgen` -a will list all the aliases you could run.

`compgen` -b will list all the built-ins you could run.

`compgen` -k will list all the keywords you could run.

`compgen` -A function will list all the functions you could run.

`compgen` -A function -abck will list all the above in one go.

* `man` Shows a command’s manual

## Directories

* `ls` Lists a directory’s content
* `pwd` Shows the current working directory’s path
* `cd` Changes the working directory
* `mkdir` Creates a new directory
* `rmdir` Deletes directories

## Files

* `touch` Creates a new empty file
* `rm` Deletes a file or directories
* `cp` Copies files and directories, including their content
* `mv` Moves or renames files and directories
* `file` Checks a file’s type
* `tree` folder structure [not built-in]

## Compression

* `zip` and `unzip` Creates and extracts a ZIP archive
* `tar` Archives files without compression in a TAR format
* `gzip` Manipulate archives with .gz extension.s
* `bzip` and `bunzip2` Manipulate archives with .bz2 extension.

### Examples

`tar -v` Get verbose output while manipulating TAR archives. May combine this option with others, e.g., tar -tvf.

`tar -cf archive.tar` Create a TAR archive named archive.tar containing Y.

`tar -xf archive.tar` Extract the TAR archive named archive.tar.

`tar -tf archive.tar` List contents of the TAR archive named archive.tar.

`tar -czf archive.tar.gz` Create a gzip-compressed TAR archive named archive.tar.gz containing Y.

`tar -xzf archive.tar.gz` Extract the gzip-compressed TAR archive named archive.tar.gz.

`tar -cjf archiave.tar.bz2` Create a bzip2-compressed TAR archive named archive.tar.bz2 containing Y.

`tar -xjf archive.tar.bz2` Extract the bzip2-compressed TAR archive named archive.tar.bz2.

`gzip Y` Create a gzip archive named Y.gz containing Y.

`gzip -l Y.gz` List contents of gzip archive Y.gz.

`gzip -d Y.gz` Decompress the gzip archive Y.gz.

`gunzip Y.gz` Extract Y.gz and recover the original file Y.

`bzip2 Y` Create a bzip2 archive named Y.bz2 containing Y.

`bzip2 -d Y.gz`  Decompress the bzip2 archive Y.bz2.

`bunzip2 Y.gz` Extract Y.bz2 and recover the original file Y.

`zip -r Z.zip` Zip to the ZIP archive Z.zip.

`unzip Z.zip` Unzip Z.zip to the current directory.

`unzip Z.zip` List contents of Z.zip.

## Editor

* `nano`, vi, and jed Edits a file with a text editor
* `history` Lists previously run commands
* `date` Display system time
* `cal` Displays a calendar in Terminal. (not builtin, need to install `ncal`)
* `calc` Calculator
* `vi` or `vm` Powerful text editor.
* `jed` Lightweight text editor.

Note:

Please see `vim` cheatsheet seperately.

## Profile, Configuration and Path

* `ln` Links files or directories
* `alias` and `unalias` Sets and removes an alias for a file or command
* `export` export definition of system variable
* `source` execute the system profile
* `set` Modifies shell settings and environment variables.
* `unset` Removes definitions of shell variables and functions.

### ln Examples

Creating a Hard Link

`ln original.txt hard_link.txt`

Creating a Symbolic Link

`ln -s original.txt soft_link.txt`

Differences Between Hard Links and Symbolic Links

**Hard Links:**

* Share the same inode.
* Both the original file and the hard link are indistinguishable.
* Deleting the original file does not affect the hard link.

**Symbolic Links:**

* Are separate files with their own inodes.
* Act as pointers to the original file.
* If the original file is deleted, the symbolic link becomes a broken link.

### alias, unalias examples

To make an alias permanent, add it to your shell's configuration file (`~/.bashrc` for Bash, `~/.zshrc` for Zsh, etc.):

```bash
alias ll='ls -l'
alias la='ls -a'
alias update='sudo apt-get update && sudo apt-get upgrade'
```

* Remove a Specific Alias:

`unalias ll`

* Remove All Aliases:

`unalias -a`

* Listing Aliases

`alias`

### set and unset examples

* Display All Shell Variables and Functions

`set`

* Enable a Shell Option (-):

Enable the -x option to print commands and their arguments as they are executed:

`set -x`

The set -x command is a valuable debugging tool. It prints each command and its arguments to the standard error (stderr) before executing it. This feature provides a window into the script’s behavior, helping developers understand the flow and pinpoint where things might be going wrong.

The following is the difference with and without `set -x`,

```bash
xiaofengli@xiaofenglx:~/Desktop/fserver/file_server/FamilyFinance$ vi test.sh 
xiaofengli@xiaofenglx:~/Desktop/fserver/file_server/FamilyFinance$ ./test.sh
mv: cannot stat '*.txt': No such file or directory
xiaofengli@xiaofenglx:~/Desktop/fserver/file_server/FamilyFinance$ vi test.sh 
xiaofengli@xiaofenglx:~/Desktop/fserver/file_server/FamilyFinance$ ./test.sh
+ mkdir my_directory
mkdir: cannot create directory ‘my_directory’: File exists
+ mv '*.txt' my_directory/
mv: cannot stat '*.txt': No such file or directory
```

* Disable a Shell Option (+):

`set -x` will print more information on the screen thus creates vulnerability,

to solve that, we can use `+x` to stop it, and then turn it on again,

`set +x`

For example,

```bash
Mitigating the Risk
To mitigate this risk, you can temporarily turn off set -x when executing commands that handle sensitive information:

#!/bin/bash
set -x
# Some non-sensitive commands
set +x
password="my_secret_password"
set -x
# More non-sensitive commands
```

* `set -e`

On the other hand, set -e tells the shell to exit the script if any command returns a non-zero exit status (an indication of failure in Unix-like systems). This command is crucial for robust error handling.

For example,

```bash
#!/bin/bash
set -e

echo "Updating system..."
sudo apt-get update

echo "Installing important package..."
sudo apt-get install -y important-package

echo "Configuring system..."
sudo cp /etc/some/config /etc/some/other/config

echo "Script completed!"
```

Will output,

```
Updating system...
script.sh: line 5: apt-get: command not found
```

* `set -u`

-u will alert and complaint any unset variables that is being referenced.

* Define Positional Parameters

`set -- arg1 arg2 arg3`

After running this command, $1 will be arg1, $2 will be arg2, and $3 will be arg3. For example,

```bash
# myvar="This is a testing"
# set -- $myvar
# echo $1
# echo $2
# echo $3
# echo $4
```

* unset variable

`unset MY_VAR`

* Unset Shell Option:

`set +x`

* Unset Positional Parameters

`unset --`

## Permissions

* `sudo` Runs a command as a superuser
* `su` Runs programs in the current shell as another user
* `chmod` Modifies a file’s read, write, and execute permissions
* `chown` Changes a file, directory, or symbolic link’s ownership
* `useradd` and `userdel` Creates and removes a user account

### Examples

`chmod permission file` Change permissions of a file or directory. 

```bash
Permissions may be of the form [u/g/o/a][+/-/=][r/w/x] (see examples below) 
or a three-digit octal number.
```

- `chown user2 file` Change the owner of a file to user2.

- `chgrp group2 file` Change the group of a file to group2.


**Numeric Representation**

The table below compares Linux file permissions in octal form and in the format [u/g/o/a][+/-/=][r/w/x].

```bash
OCTAL	PERMISSION(S)	EQUIVALENT TO APPLICATION OF
0	No permissions	-rwx
1	Execute permission only	=x
2	Write permission only	=w
3	Write and execute permissions only: 2 + 1 = 3	=wx
4	Read permission only	=r
5	Read and execute permissions only: 4 + 1 = 5	=rx
6	Read and write permissions only: 4 + 2 = 6	=rw
7	All permissions: 4 + 2 + 1 = 7	=rwx
```

## Files Operations

* `echo` Prints a message as a standard output
* `cat` Lists, combines, and writes a file’s content as a standard output
* `less` Read file
* `more`  Read file
* `head` Displays a file’s first ten lines
* `tail` Prints a file’s last ten lines
* `sort` Reorders a file’s content
* `cut` Sections and prints lines from a file
* `diff` Compares two files’ content and their differences
* `tee` Prints command outputs in Terminal and a file
* `wc`   counting utility
* `tr`  is used to translate, squeeze, and delete characters from the standard input and write the result to the standard output.
* `rev` is used to reverse the order of characters in every line of a file or from standard input.
* `sed`  Stream Editor. Perform text transformations on an input stream.
* `awk`  Pattern scanning and text processing language.

### more examples

`more -n 5 file.txt`: show the first 5 lines

`more +20 file.txt`: show starting from the 20th line

`more -f file.txt`: This option enables the continuous display of the contents of a file.

### tee examples

`wc -l file1.txt|tee -a file2.txt`

file1.txt

Input: geek
       for
       geeks

file2.txt

Input:geeks
      for
      geeks
OUTPUT : 3 file1.txt

cat file2.txt
OUTPUT:
      geeks
      for
      geeks
      3 file1.txt

`wc -l file1.txt| tee file2.txt`
will overwrite the output to fil2.txt

### cut examples

```bash
touch words.txt

happy
world
hello John

List without ranges:

cut -b 1,2,3 state.txt

cut -b 1-3,5-7 state.txt
```

Special Form: Selecting bytes from beginning to end of line
In this, 1- indicate from 1st byte to end byte of a line

`cut -b 1- state.txt`

In this, -3 indicate from 1st byte to 3rd byte of a line

`cut -b -3 state.txt`

Cut by Character (-c) Using cut Command

-c (column): To cut by character use the -c option. This selects the characters given to the -c option. This can be a list of numbers separated comma or a range of numbers separated by hyphen(-).

Tabs and backspaces are treated as a character. It is necessary to specify list of character numbers otherwise it gives error with this option.

Syntax:

`cut -c [(k)-(n)/(k),(n)/(n)] filename`

Extract specific characters:

`cut -c 2,5,7 state.txt`

Extract first seven characters:

`cut -c 1-7 state.txt`

Above command prints starting from first character to end.

`cut -c -5 state.txt`

Above command prints starting position to the fifth character.

Cut by Field (-f) Using cut Command

-f (field): -c option is useful for fixed-length lines. Most unix files doesn’t have fixed-length lines. To extract the useful information you need to cut by fields rather than columns. List of the fields number specified must be separated by comma. Ranges are not described with -f option. cut uses tab as a default field delimiter but can also work with other delimiter by using -d option.

`cut -f 1 state.txt`

If `-d` option is used then it considered space as a field separator or delimiter:

`cut -d " " -f 1 state.txt`

Extract fields 1 to 4:
Command prints field from first to fourth of each line from the file.

`cut -d " " -f 1-4 state.txt`

ref: <https://www.geeksforgeeks.org/cut-command-linux-examples/>

### sort examples

Sure, here's a simple example of using the `sort` command in Linux:

Let's say you have a file called `names.txt` with the following content:

```
John
Alice
Bob
Zoe
```

To sort the names alphabetically, you can use the `sort` command like this:

`sort names.txt`

This will output:

```
Alice
Bob
John
Zoe
```

By default, `sort` sorts lines of text in ascending order, which means alphabetically for strings. If you want to sort in descending order, you can use the `-r` option:

```
sort -r names.txt
```

This will output:

```
Zoe
John
Bob
Alice
```

You can also use `sort` to sort the output of a command. For example, if you have a list of numbers stored in a file called `numbers.txt`, you can sort them like this:

`cat numbers.txt | sort -`

This will sort the numbers numerically in ascending order. If you want to sort them in descending order, you can use:

`cat numbers.txt | sort -n -r`

### sed examples

`sed 's/old/new/' file.txt`         Substitute (replace) text

`sed '/pattern/i\new line of text' file.txt`       Insert text before a line

### tr examples

`echo "hello world" | tr 'a-z' 'A-Z'`              Translate lowercase to uppercase

`echo "hello 123 world" | tr -d '0-9'`             Delete specific characters

### awk examples

`awk '{print $1, $3}' file.txt`                   Print specific columns

`awk '{sum += $1} END {print sum}' file.txt`       Sum the values of a column

### rev examples

`echo "hello" | rev`                              Reverse a single line

`rev file.txt`                                    Reverse the content of a file

### grep examples

```bash
grep patt /path/to/src	Search for a text pattern patt in X. Commonly used with pipe e.g., ps aux | grep python3 filters out the processes containing python3 from all running processes of all users.
grep -r patt /path/to/src	Search recursively (the target directory /path/to/src and its subdirectories) for a text pattern patt.
grep -v patt X	Return lines in X not matching the specified patt.
grep -l patt X	Write to standard output the names of files containing patt.
grep -i patt X	Perform case-insensitive matching on X. Ignore the case of patt.
```

## Search

* `find` used to search for files and directories in a directory hierarchy based on various criteria like name, type, size, and modification time.

* `locate` command searches for files in a prebuilt database. It is faster than find because it searches through a database instead of the actual filesystem.

### find and locate examples

```bash
find Find files.
find /path/to/src -name "*.sh"	Find all files in /path/to/src matching the pattern "*.sh" in the file name.
find /home -size +100M	Find all files in the /home directory larger than 100MB.
locate name	Find files and directories by name.
```

## File transfer

* `ssh` Secure Shell; used to log into a remote machine and execute commands
* `scp` Securely copies files or directories to another system
* `rsync` Synchronizes content between directories or machines
* sftp secured ftp

### Examples

```bash
ssh user@access	Connect to access as user.
ssh access	Connect to access as your local username.
ssh -p port user@access	Connect to access as user using port.
scp [user1@]host1:[path1] [user2@]host2:[path2]	Login to hostN as userN via secure copy protocol for N=1,2.

Example usage:
scp alice@pi:/home/source bob@arduino:/destination

path1 and path2 may be local or remote, but ensure they’re absolute rather than relative paths, e.g., /var/www/*.html, /usr/bin.

If user1 and user2 are not specified, scp will use your local username.
scp -P port [user1@]host1:[path1] [user2@]host2:[path2] Connect to hostN as userN using port for N=1,2.
scp -r [user1@]host1:[path1] [user2@]host2:[path2] Recursively copy all files and directories from path1 to path2.
sftp [user@]access Login to access as user via secure file transfer protocol. If user is not specified, your local username will be used.
sftp access	Connect to access as your local username.
sftp -P port user@access Connect to access as user using port.
rsync -a [path1] [path2] Synchronize [path1] to [path2], preserving symbolic links, attributes, permissions, ownerships, and other settings.
rsync -avz host1:[path1] [path2] Synchronize [path1] on the remote host host1 to the local path [path2], preserving symbolic links, attributes, permissions, ownerships, and other settings. It also compresses the data involved during the transfer.
```

## System Information

* `df` Displays the system’s overall disk space usage
* `du` Checks a file or directory’s storage consumption
* `top` Displays running processes and the system’s resource usage
* `vmstat`  Report virtual memory statistic
* `htop` Works like top but with an interactive user interface (not default command)
* `ps` Creates a snapshot of all running processes
* `uname` Prints information about your machine’s kernel, name, and hardware
* `hostname` Shows your system’s hostname
* `time` Calculates commands’ execution time
* `watch` Runs another command continuously
* `jobs` Displays a shell’s running processes with their statuses
* `kill` Terminates a running process
* `bg` Resumes a suspended job in the background.
* `fg` Brings a background job to the foreground
* `pidof` Finds the process ID of a running program.
* `nice` Runs a command with a modified scheduling priority.
* `renice`  Changes the priority of a running process.
* `lsof` List All Open Files
* `which` Find file location which is on the path
* `whomai` Currently logged-in user
* `id` Displays user and group information.
* `uptime` Time system has been up since last reboot
* `shutdown` Turns off or restarts the system
* `reboot`  Reboot
* `systemctl` Manages system services
* `halt` Stop the system immediately.
* `su` Switches the current user to another user.
* `sudo` Superuser; use this before a command that requires root access e.g., su shutdown
* `last reboot` Show reboot history.

```bash
COMMAND	  DESCRIPTION

`uname -a` Detailed Linux system information

`uname -r` Kernel release information, such as kernel version

`hostname -I` Display IP address of host

`cat /etc/*-release` Show the version of the Linux distribution installed. For example, if you’re using Red Hat Linux, you may replace * with redhat.
```

## Hardware

These commands provide details about the hardware supporting your Linux machine.

* `dmesg` Display messages in kernel ring buffer (data structure that records messages related to the operation of the program running the operating system)
* `/proc/cpuinfo` CPU information
* `/proc/meminfo`  Memory information 
* `dmidecode` Display system hardware components, serial numbers, and BIOS version
* `hdparm`  Display information about the disk
* `badblocks` Test for unreadable blocks

### cpu, memory info examples

`cat /proc/cpuinfo`

`cat /proc/meminfo`

### Display PCI devices examples

`lspci -tv` Displays information about each Peripheral Component Interconnect (PCI) device on your system.
            The option -t outputs the information as a tree diagram, and -v is for verbose output.

### Display USB devices examples

`lsusb -tv`  Display information about Universal Serial Bus (USB) devices and the devices connected to them.
            The option -t outputs the information as a tree diagram, and -v is for verbose output.

### Display DMI/SMBIOS (hardware info) from the BIOS examples

`dmidecode`

### Show info about disk sda examples

`hdparm -i /dev/sda`

### Perform a read speed test on disk sda examples

`hdparm -tT /dev/sda`

### Test for unreadable blocks on disk sda examples

`badblocks -s /dev/sda`

## Disk Usage

These commands provide storage details regarding your Linux machine.

* `df` Display free disk space.
* `du` Show file/folder sizes on disk.

**usage and options**

```bash
du -ah Disk usage in human readable format (KB, MB etc.)
du -sh Total disk usage of the current directory
du -h Free and used space on mounted filesystems
du -i Free and used inodes on mounted filesystems
fdisk -l List disk partitions, sizes, and types
free -h	Display free and used memory in human readable units.
free -m	Display free and used memory in MB.
free -g	Display free and used memory in GB.
```

### Examples

```bash
xiaofengli@xiaofenglx:~/code/codebank$ uname -a
Linux xiaofenglx 6.5.0-28-generic #29~22.04.1-Ubuntu SMP PREEMPT_DYNAMIC Thu Apr  4 14:39:20 UTC 2 x86_64 x86_64 x86_64 GNU/Linux

xiaofengli@xiaofenglx:~$ who
xiaofengli tty2         2024-05-03 09:13 (tty2)

xiaofengli@xiaofenglx:~$ whoami
xiaofengli

xiaofengli@xiaofenglx:~$ vmstat
procs -----------memory---------- ---swap-- -----io---- -system-- ------cpu-----
 r  b   swpd   free   buff  cache   si   so    bi    bo   in   cs us sy id wa st
 0  2      0 28084128 166644 2465256    0    0  1911    99  537 1266  7  3 12 78  0

xiaofengli@xiaofenglx:~$ free
               total        used        free      shared  buff/cache   available
Mem:        32700488     1971364    28066992      248572     2662132    30066188
Swap:        2097148           0     2097148

xiaofengli@xiaofenglx:~$ free -m
               total        used        free      shared  buff/cache   available
Mem:           31934        1966       27362         242        2604       29319
Swap:           2047           0        2047

xiaofengli@xiaofenglx:~/code/codebank$ du -m
1 ./BloggerDev
1 ./.git/branches
1 ./.git/refs/heads
1 ./.git/refs/tags
1 ./.git/refs/remotes/origin
1 ./.git/refs/remotes
1 ./.git/refs
1 ./.git/info
2 ./.git/objects/97

xiaofengli@xiaofenglx:~/code/codebank$ df
Filesystem       1K-blocks       Used  Available Use% Mounted on
tmpfs              3270052       3624    3266428   1% /run
/dev/sda2        479079112  129910872  324758848  29% /
tmpfs             16350244      46012   16304232   1% /dev/shm
tmpfs                 5120          4       5116   1% /run/lock
efivarfs               128         35         89  28% /sys/firmware/efi/efivars
/dev/sdb1      11718752252 1749660476 9969091776  15% /mnt/ntfs
/dev/sda1           523244       6220     517024   2% /boot/efi
tmpfs              3270048        140    3269908   1% /run/user/1000
```

#### lsof examples

FD – stands for a File descriptor and may see some of the values as:

* cwd current working directory
* rtd root directory
* txt program text (code and data)
* mem memory-mapped file

Also in FD column numbers like 1u is actual file descriptor and followed by u,r,w of its mode as:

- `r` for read access.
- `w` for write access.
- `u` for read and write access.
- `TYPE` – of files and it’s identification.
- `DIR` – Directory
- `REG` – Regular file
- `CHR` – Character special file.
- `FIFO` – First In First Out

```
xiaofengli@xiaofenglx:~/code/codebank$ lsof| grep -i 8080
apache2   8072 8080 apache2           www-data  cwd   unknown                                         /proc/8072/task/8080/cwd (readlink: Permission denied)
apache2   8072 8080 apache2           www-data  rtd   unknown                                         /proc/8072/task/8080/root (readlink: Permission denied)
apache2   8072 8080 apache2           www-data  txt   unknown                                         /proc/8072/task/8080/exe (readlink: Permission denied)
apache2   8072 8080 apache2           www-data NOFD                                                   /proc/8072/task/8080/fd (opendir: Permission denied)
```

*List User Specific Opened Files*

`lsof -u xiaofengli`

*Find Processes Running on Specific Port*

`lsof -i TCP:22`

*List Only IPv4 & IPv6 Open Files*

`lsof -i 4`

`lsof -i 6`

*List Open Files of TCP Port Ranges 1-1024*

`lsof -i TCP:1-1024`

*Exclude User with ‘^’ Character*

`lsof -i -u^root`

*Find Out who’s Looking What Files and Commands?*

`lsof -i -u xiaofenglx`

*List all Network Connections*

The following command with option ‘-i’ shows the list of all network connections ‘LISTENING & ESTABLISHED’.

`lsof -i`

*Search by PID*

`lsof -p 1`

Kill all Activity of Particular User

```
kill -9 `lsof -t -u tecmint`
```

## Network

* `ping` Checks the system’s network connectivity
* `wget` Downloads files from a URL
* `curl` Transmits data between servers using URLs
* `lfconfig` Displays the system’s network interfaces and their configurations
* `netstat` Shows the system’s network information, like routing and sockets
* `traceroute` Tracks a packet’s hops to its destination
* `nslookup` Queries a domain’s IP address and vice versa
* `dig` Displays DNS information, including record types

### wget examples

Get all the links recursively.

`wget -r https://docs.python.org/3/tutorial/index.html`

### curl examples

`-X`, equivalent to --method??
`-L`, same as --location
`-d`, same as --data
`-o`, --output

`curl` to send http post.

```
curl --location '192.168.1.186:9200/school*/_search' \
--header 'Content-Type: application/json' \
--data '{
   "query":{
       "match" : {
         "rating":"4.5"
      }
   }
}'
```

`curl` to do http get.

```
curl --location --request GET '192.168.1.186:9401/schools/_search' \
--header 'Content-Type: application/json' \
--data '{
   "query":{
      "match_all":{}
   }
}'
```

### netstat examples

* -a To list all listening ports, using both TCP and UDP, use `netstat -a`
* -t only tcp ports connections
* -u only udp ports connections
* -l To list all actively listening ports (both TCP and UDP)
* -s To pull and view network statistics sorted by protocol
* -p show pid
* -r The -r option of netstat displays the IP routing table
* -i To view send/receive stats by interface

Raw network stats,

`netstat --statistics --raw`

```
ssh tunnel
```

## systemctl

* `systemctl`

`Systemd` is a system and service manager for Linux; a drop-in replacement for the init process, which is compatible with SysV and LSB init scripts, and the `systemctl` command is the primary tool to manage systemd.

**Example**

`# systemctl list-units --type=service`

OR

`# systemctl --type=service`

`# systemctl list-units --type=service --state=active`
OR

`# systemctl --type=service --state=active`


<https://www.tecmint.com/list-all-running-services-under-systemd-in-linux/>

## Firewall & IPtable

<https://www.ninjaone.com/blog/how-to-configure-a-linux-firewall/#:~:text=After%20you%20configure%20a%20Linux,traffic%20based%20on%20predefined%20rules>.

## File Commands

`ln`: Creates hard and symbolic links.

Example: ln -s targetfile.txt linkname.txt  # symbolic link

`chmod`: Changes file permissions.

Example : chmod 755 myfile.txt

`chown`: Changes file owner and group.

Example : chown user:group myfile.txt

`file`: Determines the file type.

Example: file myfile.txt

`stat`: Displays file or file system status.

Example: stat myfile.txt

## File descriptor Commands

`ls -l /proc/$$/fd`: Lists open file descriptors for the current shell process.

Example: ls -l /proc/$$/fd

`lsof`: Lists open files and the processes that opened them.

Example : lsof | grep myfile.txt

`exec`: Opens a file descriptor and associates it with a command.
Example:

exec 3>outputfile.txt  # Open file descriptor 3 for writing

echo "Hello, World!" >&3  # Write to file descriptor 3

exec 3>&-  # Close file descriptor 3

`>/dev/null`: Redirects output to null device (discards output).

Example: command > /dev/null 2>&1  # Discards both standard output and standard error

`read`: Reads input from a file descriptor.

Example:

exec 3<myfile.txt  # Open file descriptor 3 for reading

read -u 3 line  # Read a line from file descriptor 3

echo $line  # Output the line read

exec 3<&-  # Close file descriptor 3

`strace`: Traces system calls and signals (including file descriptor operations).

Example: strace -e trace=file ls

## Pipe

The pipe (|) in Linux allows you to chain multiple commands together, sending the output of one command as input to another command.
`[command1] | [command 2]`

Basic Example:

`ps aux | grep python3 `: This command lists all running processes (ps aux) and pipes (|) the output to grep python3, which filters out lines containing python3.

`ls -l | wc -l` : This command lists all files in the current directory (ls -l) and pipes (|) the output to wc -l, which counts the number of lines, effectively giving the count of files in the directory.

`cat file.txt | sort` : This command reads the contents of file.txt (cat file.txt) and pipes (|) the output to sort, which sorts the lines alphabetically.
`

## Redirection

The redirect operator >, <, >>, 2>.

COMMAND              DESCRIPTION

`echo TEXT`          Display a line of TEXT or the contents of a variable.

`echo -e TEXT`       Also interprets escape characters in TEXT, e.g., \n → new line, \b → backslash, \t → tab.

`echo -n TEXT`       Omits trailing newline of TEXT.

`cmd1 | cmd2`        | is the pipe character; feeds the output of cmd1 and sends it to cmd2, e.g., ps aux | grep python3.

`cmd > file`         Redirect output of cmd to a file file. Overwrites pre-existing content of file.

`cmd >& file`        Redirect output of cmd to file. Overwrites pre-existing content of file. Suppresses the output of cmd.

`cmd > /dev/null`    Suppress the output of cmd.

`cmd >> file`        Append output of cmd to file.

`cmd < file`         Read input of cmd from file.

`cmd << delim`       Read input of cmd from the standard input with the delimiter character delim to tell the system where to terminate the input. Example for counting the number of lines of ad-hoc input:

```bash
wc -l << EOF
I like
apples
and
oranges.
EOF
```

Hence there are only 4 lines in the standard input delimited by EOF.

`cmd <<< string` Input a text string to cmd.

`cmd 2> foo`     Redirect error messages of cmd to foo.

`cmd 2>> foo`    Append error messages of cmd to foo.

`cmd &> file`    Redirect output and error messages of cmd to file.

`cmd &>> file`   Append output and error messages of cmd to file.

## Package and software management (debian)

* `apt`  A command-line utility for handling package management in Debian-based distributions.
* `apt-get` Manages Debian-based distros package libraries
* `dpkg`    dpkg is a medium-level tool to install, build, remove and manage Debian packages.

### apt and apt-get examples

The apt command line tool provides a higher-level user interface for end users with intuitive commands, resulting behaviors, and security features. In contrast, the command apt-get is a low-level interface that communicates more closely with core Linux processes. The apt command is a more user-friendly package manager than apt-get.

Used in Linux-based operating systems to update the package lists for available software packages from the configured repositories.

`sudo apt-get upgrade`

This command is used to install the latest versions of the packages currently installed on the user’s system from the sources enumerated in /etc/apt/sources.list. The installed packages which have new packages available are retrieved and installed. You need to perform an update before the upgrade so that apt-get knows that new versions of packages are available.

`sudo apt-get install [package_name]`

This command is used to install or upgrade packages.

`sudo apt-get remove [package_name]`

Remove software but does not remove configuration files

`sudo apt-get purge [package_name]`

Remove software and remove configuration files

`sudo apt-get check`

This command is used to update the package cache and check for broken dependencies.

`sudo apt-get clean`

This command is used to keep our system clean and tidy. It removes all the cached package files that were downloaded due to the downloading of recent packages using `apt-get`.

`sudo apt-get autoremove`

Sometimes the packages which are automatically installed to satisfy the dependencies of other packages, are no longer needed then the autoremove command is used to remove this kind of packages.

`sudo apt-get list`

It also gives details (version, architecture and repository source) about package but only if package is available or installed in our system. `sudo apt-get list firefox`

To get more options, check with -h,


Most used commands:
  `update` - Retrieve new lists of packages

  `upgrade` - Perform an upgrade

  `install` - Install new packages (pkg is libc6 not libc6.deb)

  `reinstall` - Reinstall packages (pkg is libc6 not libc6.deb)

  `remove` - Remove packages

  `purge` - Remove packages and config files

  `autoremove` - Remove automatically all unused packages

  `dist-upgrade` - Distribution upgrade, see apt-get(8)

  `dselect-upgrade` - Follow dselect selections

  `build-dep` - Configure build-dependencies for source packages

  `satisfy` - Satisfy dependency strings

  `clean` - Erase downloaded archive files

  `autoclean` - Erase old downloaded archive files

  `check` - Verify that there are no broken dependencies

  `source` - Download source archives

  `download` - Download the binary package into the current directory

  `changelog` - Download and display the changelog for the given package


### dpkg examples


  `install`
      The package is selected for installation.

  `hold`
      A package marked to be on hold is kept on the same version, that is, no automatic new
      installs, upgrades or removals will be performed on them, unless these actions are
      requested explicitly, or are permitted to be done automatically with the --force-hold
      option.

  `deinstall`
      The package is selected for deinstallation (i.e. we want to remove all files, except
      configuration files).

  `purge`
      The package is selected to be purged (i.e. we want to remove everything from system
      directories, even configuration files).

  `unknown`
      The package selection is unknown.  A package that is also in a not-installed state, and
      with an ok flag will be forgotten in the next database store.

## Ref

* <https://man7.org/tlpi/index.html>
* <https://www.dpkg.org/>
* <https://manpages.ubuntu.com/manpages/trusty/man1/dpkg.1.html>
* <https://tldp.org/>
* <https://github.com/tLDP>
* <https://www.linuxdoc.org/>
* <https://www.linux.com/training-tutorials/linux-documentation-project/>
* <https://linux.die.net/man/7/ldp>
* <https://docs.kernel.org/>
* https://devhints.io/bash