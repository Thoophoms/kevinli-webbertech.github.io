# Neo4j Installation

## Install from source code

Please refer to the following link,

[Install from tarball](https://neo4j.com/docs/operations-manual/current/installation/linux/tarball/)

## Install from Ubuntu

**How to install Neo4j**

The first thing you’ll want to do is update and upgrade your server. Remember, if the kernel is upgraded, you must reboot the server for the changes to take effect. Because of that, you might want to hold off on upgrading until such a time as the server can safely be rebooted. If this isn’t a production server, you can do it any time you like.

To update and upgrade Ubuntu, log in to your server and issue the command:

`sudo apt-get update && sudo apt-get upgrade -y`

When the upgrade is finished, reboot if necessary.

Once the upgrade is completed, install the Neo4j dependencies with the command:

```bash
sudo apt-get install wget curl nano software-properties-common dirmngr apt-transport-https gnupg gnupg2 ca-certificates lsb-release ubuntu-keyring unzip -y
```

Next, you must add the official Neo4j GPG key with the command:

```bash
curl -fsSL https://debian.neo4j.com/neotechnology.gpg.key | sudo gpg --dearmor -o /usr/share/keyrings/neo4j.gpg
```

Add the Neo4j repository with:

```bash
echo "deb [signed-by=/usr/share/keyrings/neo4j.gpg] https://debian.neo4j.com stable latest" | sudo tee -a /etc/apt/sources.list.d/neo4j.list
```

Update apt with:

`sudo apt-get update`

Finally, install Neo4j with the command:

`sudo apt-get install neo4j -y`

When the installation is complete, start and enable the service with:

`sudo systemctl enable --now neo4j`

**How to enable Neo4j connections from beyond localhost**

At the moment, the only machine allowed to connect to the Neo4j server is localhost. If you’ll be using the database from machines other than the one it’s installed on, you’ll want to enable remote connections. To do that, open the Neo4j configuration file for editing with:

`sudo nano /etc/neo4j/neo4j.conf`

In that file, look for the following line:

`#server.default_listen_address=0.0.0.0`

Remove the #, so the line now reads:

`server.default_listen_address=0.0.0.0`

Save and close the file with the CTRL+X keyboard shortcut. Restart the Neo4j service with:

`sudo systemctl restart neo4j`

You must also edit the system hosts file. To do that, issue the command:

`sudo nano /etc/hosts`

At the bottom of the file, add a line like this:

`SERVER_IP HOSTNAME`

Where SERVER_IP is the IP address of the hosting server and HOSTNAME is the hostname of the machine. Save and close the file. For example, if your IP address is 192.168.1.7 and your hostname is fossa, the line would be:

`192.168.1.7 fossa`

**How to test the Neo4j connection**

To test the Neo4j connection, the command would look something like this:

`cypher-shell -a 'neo4j://192.168.1.7:7687'`

Both the default username and password are neo4j. After typing the default password, you’ll be prompted to create a new one. Once you’ve done that, you’ll find yourself at the Neo4j console.

If the connection fails, you might have to open the firewall on the server. To do that, you’ll also want to know the IP address of any machine that will connect to the server. For example, if you’re connecting from IP address 192.168.1.100, you could open the firewall with the command:

`sudo ufw allow from 192.168.1.62 to any port 7687 proto tcp`

If you want to open the connection to any machine on your network, that command might look like this:

`sudo ufw allow from 192.168.1.0/24 to any port 7687 proto tcp`