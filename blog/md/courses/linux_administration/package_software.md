# Linux Software and Package Installation

## Overview

* You will learn `apt` package management in ubuntu
* Configuring `apt` Repositories in Ubuntu

>Hint: Fedora core package management will be skipped

## **Ubuntu Package Installation**

Ubuntu uses `apt` (Advanced Package Tool) for managing software packages. Below are essential commands for installing, updating, and managing packages.

---

### **1. Updating Package Lists**

Before installing any package, update the package list to ensure you get the latest versions:

* Purpose: Updates the list of available packages and versions from configured repositories.
* Does not install or upgrade any software, just refreshes metadata.

```bash
sudo apt update
```

To upgrade all installed packages:

```bash
sudo apt upgrade -y
```

---

### **2. Installing a Package**

To install a package (e.g., `curl`):

```bash
sudo apt install curl -y
```

Install multiple packages at once:

```bash
sudo apt install git vim wget -y
```

---

### **3. Removing a Package**

To remove a package:
```bash
sudo apt remove package_name -y
```

For example:

```bash
sudo apt remove apache2 -y
```

To remove a package along with configuration files:

```bash
sudo apt purge package_name -y
```

---

### **4. Searching for a Package**

To search for a package:
```bash
apt search package_name
```

Example:

```bash
apt search nginx
```

---

### **5. Listing Installed Packages**

To list all installed packages:

```bash
dpkg --list
```

To check if a specific package is installed:

```bash
dpkg -l | grep package_name
```

---

### **6. Checking Package Information**

To view details of a package:
```bash
apt show package_name
```

Example:

```bash
apt show python3
```

---

### **7. Installing a `.deb` Package**

If you have a `.deb` package, install it with:

```bash
sudo dpkg -i package_name.deb
```

If there are dependency issues, fix them with:

```bash
sudo apt --fix-broken install
```

---

### **8. Removing Unused Packages**

To clean unnecessary dependencies:

```bash
sudo apt autoremove -y
```

To clear the package cache:

```bash
sudo apt clean
```

---

### **9. `apt purge` in Ubuntu**

The `apt purge` command is used to **completely remove a package** along with its configuration files. This is different from `apt remove`, which only removes the package but keeps its configuration files.


1. **Purge a single package:**

   ```bash
   sudo apt purge package_name -y
   ```

   Example:
   ```bash
   sudo apt purge apache2 -y
   ```
   This removes `apache2` and its associated configuration files.

2. **Purge multiple packages:**
   ```bash
   sudo apt purge package1 package2 -y
   ```

   Example:
   ```bash
   sudo apt purge nginx mysql-server -y
   ```

3. **Purge unnecessary dependencies:**

   ```bash
   sudo apt autoremove --purge -y
   ```

   This removes packages that are no longer needed, along with their configuration files.

4. **Purge a package and clean up:**

   ```bash
   sudo apt purge package_name -y && sudo apt autoremove --purge -y && sudo apt clean
   ```

   This ensures complete removal and cleanup.

### **10. `apt full-upgrade` (Complete System Upgrade)**

Purpose: Upgrades all installed packages and removes conflicting dependencies.

`sudo apt full-upgrade -y`

**When to use?**

When upgrading major system components (e.g., a new Ubuntu release) where dependencies need to be replaced.

## **Configuring `apt` Repositories in Ubuntu**  

APT repositories are sources for downloading and installing software packages. These repositories are defined in configuration files located in `/etc/apt/`.

---

### **1. Checking Existing Repositories**

To list all currently configured repositories:

```bash
cat /etc/apt/sources.list
```

or

```bash
grep -r '^deb' /etc/apt/sources.list /etc/apt/sources.list.d/
```

---

### **2. Adding a New Repository**

Repositories are listed in `/etc/apt/sources.list`. You can manually edit this file or use the following methods:

#### **a) Manually Editing `sources.list`**

Open the file using:

```bash
sudo nano /etc/apt/sources.list
```

Add a new repository entry, for example:

```
deb http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse
deb-src http://archive.ubuntu.com/ubuntu focal main restricted universe multiverse
```

Save and exit (`CTRL+X`, then `Y` and `Enter`).

#### **b) Using `add-apt-repository` Command**

To add a Personal Package Archive (PPA):

```bash
sudo add-apt-repository ppa:graphics-drivers/ppa
```

Then update package lists:

```bash
sudo apt update
```

#### **c) Adding a Third-Party Repository**

1. Add the repository key:

   ```bash
   wget -qO - https://download.example.com/public.key | sudo apt-key add -
   ```

2. Add the repository URL:

   ```bash
   echo "deb http://download.example.com/ubuntu focal main" | sudo tee /etc/apt/sources.list.d/example.list
   ```

3. Update package lists:

   ```bash
   sudo apt update
   ```
---

### **3. Removing a Repository**

- **Using `add-apt-repository`**  

  ```bash
  sudo add-apt-repository --remove ppa:graphics-drivers/ppa
  ```

- **Manually Removing from `sources.list.d`**  

  ```bash
  sudo rm /etc/apt/sources.list.d/example.list
  ```

- **Disabling a Repository (Instead of Deleting)**  
  Edit the repository file and comment out (`#`) the repository line.

---

### **4. Fixing Broken Repositories**

If you experience issues after modifying repositories, try:

```bash
sudo apt --fix-broken install
sudo apt update --fix-missing
```
