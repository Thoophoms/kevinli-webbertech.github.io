# K8s Portforwarding

## Connect to RDS using SSH Tunnel

To access an RDS (Relational Database Service) instance running on AWS from your local computer, you typically follow these steps:

### Prerequisites:
- **AWS RDS instance**: Ensure that you have an RDS instance already set up.
- **Security Group Configuration**: Make sure the security group associated with the RDS instance allows inbound traffic on the port used by the database (usually port 3306 for MySQL, 5432 for PostgreSQL, etc.). You'll need to open the port for your local IP address or a specific range of IP addresses.

### Step-by-Step Instructions:

#### 1. **Find RDS Endpoint and Port:**
   - Go to the AWS Management Console.
   - Navigate to **RDS** and select the database instance.
   - Copy the **Endpoint** (a URL) and the **Port** number (default is 3306 for MySQL, 5432 for PostgreSQL, etc.).

#### 2. **Modify the RDS Security Group:**
   - In the **EC2 Dashboard** (where security groups are managed), locate the security group attached to the RDS instance.
   - Edit the inbound rules of the security group to allow traffic from your local machine's IP address.
     - **Type**: Custom TCP Rule (or the type specific to your DB, e.g., MySQL/Aurora, PostgreSQL)
     - **Port Range**: Enter the database port (e.g., 3306 for MySQL).
     - **Source**: Your IP address (e.g., `203.0.113.0/32` if your IP is `203.0.113.0`).

#### 3. **Set up a Database Client:**

   - Install a database client (like **MySQL Workbench**, **pgAdmin**, or a command-line client like **MySQL CLI** or **psql**).
   - Use the following connection details to access the database:
     - **Host**: The RDS endpoint (e.g., `mydbinstance.cxj3s7v2ddvf.us-west-2.rds.amazonaws.com`).
     - **Port**: The port of your database (e.g., `3306` for MySQL, `5432` for PostgreSQL).
     - **Database name**: The name of your database.
     - **Username**: The master username for your RDS instance.
     - **Password**: The master password for your RDS instance.

#### 4. **Test the Connection:**
   - Open your database client and attempt to connect to the RDS instance using the connection details. If configured correctly, you should be able to access and query the database remotely.

#### Example Command (for MySQL CLI):

```bash
mysql -h mydbinstance.cxj3s7v2ddvf.us-west-2.rds.amazonaws.com -P 3306 -u myusername -p
```

#### 5. **Optional - Use SSH Tunneling (If Security Group Is Restrictive):**

   If you cannot open the RDS port to your IP for security reasons, you can use an **SSH tunnel** through an EC2 instance in the same VPC as the RDS instance.

   - **Set up an EC2 instance** with a security group that allows SSH access.
   - SSH into the EC2 instance and create a tunnel to the RDS instance.
   - Use a command like this:
     ```bash
     ssh -L 3306:rds-endpoint:3306 ec2-user@ec2-public-ip
     ```
   - This will forward the RDS traffic from your local machine to the EC2 instance, which can then communicate with the RDS database.

## Connect to RDS using Portforwarding

To connect to an RDS database through Kubernetes using `kubectl port-forwarding`, you can set up port forwarding from a pod running in your Kubernetes cluster to your local machine. Once the port is forwarded, you can access the RDS instance as if it were running locally.

Here’s how you can do it:

### Prerequisites:

- **Kubernetes cluster**: You need to have access to the Kubernetes cluster with `kubectl` installed and configured.
- **RDS instance**: The RDS instance should be running and accessible from the Kubernetes cluster (make sure the RDS security group allows access from the cluster's VPC).
- **Pod with necessary database client**: You should have a pod running in your cluster that has the database client installed (e.g., MySQL client, psql for PostgreSQL, etc.).

### Step-by-Step Instructions:

#### 1. **Choose a Pod for Port Forwarding**
   You’ll need a pod that is running inside the Kubernetes cluster that can connect to the RDS instance. This could be a pod that has a database client installed, or you can use an existing pod with access to the internet and a database client.

   If you don’t have a pod with a database client, you can use a temporary pod. For example, to run a MySQL client pod in your cluster:

   ```bash
   kubectl run -i --tty --rm mysql-client --image=mysql:5.7 --restart=Never --env="MYSQL_HOST=rds-endpoint" --env="MYSQL_PORT=3306" --env="MYSQL_USER=myusername" --env="MYSQL_PASSWORD=mypassword"
   ```

   Replace `rds-endpoint`, `myusername`, and `mypassword` with your actual RDS endpoint, username, and password.

#### 2. **Set Up Port Forwarding**
   To access the RDS instance through `kubectl` port forwarding, run the following command:

   ```bash
   kubectl port-forward pod/<pod-name> <local-port>:<remote-port>
   ```

   - `<pod-name>`: The name of the pod where the client is installed (or the pod you're running).
   - `<local-port>`: The local port on your machine that you will use to connect (e.g., `3306` for MySQL).
   - `<remote-port>`: The port the pod is listening on (for database access, this would be the port of the RDS service, e.g., `3306` for MySQL, `5432` for PostgreSQL).

   Example command for MySQL:
   ```bash
   kubectl port-forward pod/mysql-client 3306:3306
   ```

   After running this, the local port `3306` on your computer will be forwarded to the pod’s `3306` port, allowing you to connect to the RDS instance via your local machine.

#### 3. **Connect to the RDS Database**
   Now, you can connect to the RDS instance using the forwarded port. For example, with a MySQL client:

   ```bash
   mysql -h 127.0.0.1 -P 3306 -u myusername -p
   ```

   For PostgreSQL, the command would be:

   ```bash
   psql -h 127.0.0.1 -p 3306 -U myusername -d mydatabase
   ```

   Replace `myusername`, `mypassword`, and `mydatabase` with the appropriate credentials and database name.

#### 4. **Access RDS from Local Machine**

   After running `kubectl port-forward`, you are able to access the RDS database as if it's running locally. The connection is forwarded through the pod, so traffic to the pod’s local port gets routed to your RDS instance.

### Optional: Troubleshooting

If you encounter any issues:

- Ensure that your Kubernetes pod has network access to the RDS instance (check the VPC and security groups).
- Double-check the credentials you are using to connect to RDS (username, password, database name).
- If there are issues with the port-forwarding, check if any firewall rules or Kubernetes network policies are blocking traffic.
