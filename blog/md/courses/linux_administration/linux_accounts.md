# **Linux Account Management Commands**

Here are essential commands for managing user accounts in Linux:

## **1. Creating a User**

```bash
sudo useradd -m username
```
- `-m` creates a home directory for the user.

## **2. Setting Password for a User**

```bash
sudo passwd username
```

## **3. Deleting a User**

```bash
sudo userdel -r username
```

- `-r` removes the user's home directory.

## **4. Disabling (Locking) a User Account**

```bash
sudo usermod -L username
```

- Locks the account to prevent login.

## **5. Enabling (Unlocking) a User Account**

```bash
sudo usermod -U username
```

## **Important `/etc` Files for User and Group Management**

| File | Description |
|------|-------------|
| `/etc/passwd` | Stores user account information. |
| `/etc/shadow` | Stores encrypted passwords. |
| `/etc/group` | Stores group information. |
| `/etc/gshadow` | Stores secure group data. |

## **View Users from `/etc/passwd`**

```bash
cat /etc/passwd | cut -d: -f1
```

## **View Groups from `/etc/group`**

```bash
cat /etc/group | cut -d: -f1
```
