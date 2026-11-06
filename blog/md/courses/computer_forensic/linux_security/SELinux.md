# **What is SELinux?**

**SELinux (Security-Enhanced Linux)** is a **mandatory access control (MAC)** system implemented in Linux to provide a robust security framework. It is designed to enforce the **principle of least privilege** by restricting processes to only the files, resources, and capabilities they absolutely need. SELinux is primarily used to control access to system resources based on security policies, rather than relying solely on traditional discretionary access control (DAC) mechanisms (e.g., file permissions).

SELinux was originally developed by the **National Security Agency (NSA)** in collaboration with other contributors to improve Linux's security, and it is included in most major Linux distributions like **Red Hat Enterprise Linux (RHEL)**, **CentOS**, and **Fedora**.

---

### **Key Features of SELinux**

1. **Fine-grained Access Control**:
   - SELinux provides more granular control over the system than traditional **user-based access control** (UBAC). It uses **security contexts** to assign security labels to objects (files, processes, ports) and decides who can interact with them.

2. **Enforcement of Security Policies**:
   - SELinux allows administrators to define policies for how processes and users interact with system objects. These policies are enforced by the **kernel**, ensuring that only authorized actions are allowed based on the labels assigned to objects and processes.

3. **Types of Policies**:
   - **Targeted Policy**: Only specific high-risk processes are confined by SELinux, with the rest of the system operating normally. This is the most common policy and is typically used in **RHEL** and **CentOS**.
   - **Strict Policy**: A more restrictive policy where **all processes** are confined by SELinux. This provides stronger security but can be more difficult to manage and requires careful configuration.
   - **MLS (Multi-Level Security)**: This policy applies more complex access control rules, usually in government or high-security environments.

4. **Enforcement Modes**:
   SELinux has three main modes that control how policies are enforced:

   - **Enforcing Mode**: The SELinux policies are actively enforced. Any action that violates the defined policy is denied.
   - **Permissive Mode**: Policies are not enforced, but any violations are logged. This mode is typically used for debugging or troubleshooting.
   - **Disabled Mode**: SELinux is completely turned off, and no policies are enforced or logged.

5. **Context-based Security**:
   - SELinux assigns a **security context** (label) to every object (files, directories, processes, etc.). The context typically includes:
     - **User**: Who owns the process or object (e.g., `user_u`).
     - **Role**: The role the process or user performs (e.g., `object_r`).
     - **Type**: The type of object or process (e.g., `httpd_t` for Apache web server processes).
     - **Level**: The sensitivity of the resource (used in **MLS** policy for high-level security).

---

### **How SELinux Works**

SELinux operates by applying security policies to every action taken on the system, controlling which processes can access which resources. Here's a basic flow of how SELinux works:

1. **Security Contexts**:
   Every process and file in the system is assigned a security context that defines its security label. For example:
   - A process running the **Apache web server** might have the context `system_u:system_r:httpd_t`, indicating that it is a system process running under the Apache service.
   - Files served by Apache (such as HTML files in `/var/www`) will have a context like `system_u:object_r:httpd_sys_content_t`.

2. **Policy Rules**:
   SELinux defines **policies** that describe which interactions are allowed between different types of objects. For example, an Apache process (with the type `httpd_t`) may be allowed to read files labeled `httpd_sys_content_t`, but it may not have the permission to write to system logs (`var_log_t`) unless explicitly allowed.

3. **Enforcement**:
   SELinux enforces the defined policies whenever a process attempts to access an object. If the access is allowed according to the policy, the action proceeds; otherwise, the action is denied, and it is logged for further inspection.

4. **Audit Logs**:
   SELinux logs access denials to a system log (usually `/var/log/audit/audit.log`). This log can be reviewed by administrators to understand why certain actions were blocked, which is helpful for troubleshooting and refining SELinux policies.

---

### **SELinux Modes and How to Change Them**

1. **Enforcing Mode**: SELinux policies are enforced, and any violation will be blocked.

   To check if SELinux is in enforcing mode:
   ```bash
   getenforce
   ```

   To switch to **enforcing** mode:
   ```bash
   sudo setenforce 1
   ```

2. **Permissive Mode**: SELinux does not enforce policies but logs violations.

   To switch to **permissive** mode:
   ```bash
   sudo setenforce 0
   ```

3. **Disabled Mode**: SELinux is completely turned off. This is not recommended unless you're troubleshooting or have specific needs for disabling SELinux.

   To permanently disable SELinux (edit `/etc/selinux/config`):
   ```bash
   sudo vi /etc/selinux/config
   ```
   Change the line:
   ```
   SELINUX=disabled
   ```

   Reboot the system for the changes to take effect.

---

### **Configuring and Managing SELinux**

#### **Checking the Status of SELinux**
To check the current status and mode of SELinux:
```bash
sestatus
```

#### **Viewing SELinux Contexts**
To view the SELinux context of a file or directory:
```bash
ls -Z /path/to/file
```

For example:
```bash
ls -Z /var/www/html
```

#### **Changing SELinux Contexts**
You can modify the SELinux context of a file or directory using the `chcon` command:
```bash
sudo chcon -t httpd_sys_content_t /var/www/html
```

This command changes the context of `/var/www/html` to `httpd_sys_content_t`, which is the appropriate type for files served by Apache.

#### **Creating Custom SELinux Policies**
If necessary, you can create custom SELinux policies to allow specific actions. This is often done when SELinux's default policies block legitimate activities (e.g., running a custom application).

To create and load a custom policy:
1. Write the policy file.
2. Compile the policy using `checkmodule`.
3. Load the policy using `semodule`.

Example:
```bash
sudo checkmodule -M -m -o mymodule.mod mymodule.te
sudo semodule_package -o mymodule.pp -m mymodule.mod
sudo semodule -i mymodule.pp
```

---

### **Common SELinux Troubleshooting and Management Tools**

1. **Audit2allow**: This tool is used to analyze SELinux audit logs and generate SELinux policy modules to allow denied actions.
   ```bash
   audit2allow -w -a
   ```

2. **semanage**: This command is used to manage SELinux policy settings, such as managing file contexts, port labeling, etc.
   Example: To allow a service to bind to a non-default port:
   ```bash
   sudo semanage port -a -t http_port_t -p tcp 8080
   ```

3. **setsebool**: This command is used to set Boolean values for SELinux policies. For example, to allow Apache to connect to the network:
   ```bash
   sudo setsebool -P httpd_can_network_connect 1
   ```

4. **getenforce** and **setenforce**: These are used to check or set the SELinux mode.
   ```bash
   getenforce
   sudo setenforce 0   # Change to Permissive Mode
   sudo setenforce 1   # Change to Enforcing Mode
   ```

---

### **Conclusion**

**SELinux** is a powerful security feature for Linux that provides **mandatory access control** and enforces policies on how processes and resources interact. By using security contexts and defining strict policies, SELinux reduces the risk of unauthorized access, privilege escalation, and other security breaches.

The primary benefits of SELinux are its ability to:
- Provide more granular and controlled access.
- Enforce security policies that go beyond traditional Linux permissions.
- Log access denials, which helps in troubleshooting and improving security.

While it can be complex to configure and manage, SELinux offers a significant layer of security, especially for critical production environments.