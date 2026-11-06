# SELinux (Security-Enhanced Linux)

Security-Enhanced Linux (SELinux) is a Linux kernel security module that provides a mechanism for supporting access control security policies, including mandatory access controls (MAC).

SELinux is a set of kernel modifications and user-space tools that have been added to various Linux distributions. Its architecture strives to separate enforcement of security decisions from the security policy, and streamlines the amount of software involved with security policy enforcement. The key concepts underlying SELinux can be traced to several earlier projects by the United States National Security Agency (NSA).

A Linux kernel integrating SELinux enforces mandatory access control policies that confine user programs and system services, as well as access to files and network resources. Limiting privilege to the minimum required to work reduces or eliminates the ability of these programs and daemons to cause harm if faulty or compromised (for example via buffer overflows or misconfigurations). This confinement mechanism operates independently of the traditional Linux (discretionary) access control mechanisms. It has no concept of a "root" superuser, and does not share the well-known shortcomings of the traditional Linux security mechanisms, such as a dependence on setuid/setgid binaries.

The security of an "unmodified" Linux system (a system without SELinux) depends on the correctness of the kernel, of all the privileged applications, and of each of their configurations. A fault in any one of these areas may allow the compromise of the entire system. In contrast, the security of a "modified" system (based on an SELinux kernel) depends primarily on the correctness of the kernel and its security-policy configuration. While problems with the correctness or configuration of applications may allow the limited compromise of individual user programs and system daemons, they do not necessarily pose a threat to the security of other user programs and system daemons or to the security of the system as a whole.

From a purist perspective, SELinux provides a hybrid of concepts and capabilities drawn from mandatory access controls, mandatory integrity controls, role-based access control (RBAC), and type enforcement architecture. Third-party tools enable one to build a variety of security policies.

## History

The earliest work directed toward standardizing an approach providing mandatory and discretionary access controls (MAC and DAC) within a UNIX (more precisely, POSIX) computing environment can be attributed to the National Security Agency's Trusted UNIX (TRUSIX) Working Group, which met from 1987 to 1991 and published one Rainbow Book (#020A), and produced a formal model and associated evaluation evidence prototype (#020B) that was ultimately unpublished.

SELinux was designed to demonstrate the value of mandatory access controls to the Linux community and how such controls could be added to Linux. Originally, the patches that make up SELinux had to be explicitly applied to the Linux kernel source; SELinux was merged into the Linux kernel mainline in the 2.6 series of the Linux kernel.

The NSA, the original primary developer of SELinux, released the first version to the open source development community under the GNU GPL on December 22, 2000.[6] The software was merged into the mainline Linux kernel 2.6.0-test3, released on 8 August 2003. Other significant contributors include Red Hat, Network Associates, Secure Computing Corporation, Tresys Technology, and Trusted Computer Solutions. Experimental ports of the FLASK/TE implementation have been made available via the TrustedBSD Project for the FreeBSD and Darwin operating systems.

Security-Enhanced Linux implements the Flux Advanced Security Kernel (FLASK). Such a kernel contains architectural components prototyped in the Fluke operating system. These provide general support for enforcing many kinds of mandatory access control policies, including those based on the concepts of type enforcement, role-based access control, and multilevel security. FLASK, in turn, was based on DTOS, a Mach-derived Distributed Trusted Operating System, as well as on Trusted Mach, a research project from Trusted Information Systems that had an influence on the design and implementation of DTOS.

Users, policies and security contexts
SELinux users and roles do not have to be related to the actual system users and roles. For every current user or process, SELinux assigns a three string context consisting of a username, role, and domain (or type). This system is more flexible than normally required: as a rule, most of the real users share the same SELinux username, and all access control is managed through the third tag, the domain. The circumstances under which a process is allowed into a certain domain must be configured in the policies. The command runcon allows for the launching of a process into an explicitly specified context (user, role, and domain), but SELinux may deny the transition if it is not approved by the policy.

Files, network ports, and other hardware also have an SELinux context, consisting of a name, role (seldom used), and type. In the case of file systems, mapping between files and the security contexts is called labeling. The labeling is defined in policy files but can also be manually adjusted without changing the policies. Hardware types are quite detailed, for instance, bin_t (all files in the folder /bin) or postgresql_port_t (PostgreSQL port, 5432). The SELinux context for a remote file system can be specified explicitly at mount time.

SELinux adds the -Z switch to the shell commands ls, ps, and some others, allowing the security context of the files or process to be seen.

Typical policy rules consist of explicit permissions, for example, which domains the user must possess to perform certain actions with the given target (read, execute, or, in case of network port, bind or connect), and so on. More complex mappings are also possible, involving roles and security levels.

A typical policy consists of a mapping (labeling) file, a rule file, and an interface file, that define the domain transition. These three files must be compiled together with the SELinux tools to produce a single policy file. The resulting policy file can be loaded into the kernel to make it active. Loading and unloading policies does not require a reboot. The policy files are either hand written or can be generated from the more user friendly SELinux management tool. They are normally tested in permissive mode first, where violations are logged but allowed. The audit2allow tool can be used later to produce additional rules that extend the policy to allow all legitimate activities of the application being confined.

## Adoption

`sestatus` showing status of SELinux in a system

[image]

SELinux has been implemented in Android since version 4.3.

Among free community-supported Linux distributions, Fedora was one of the earliest adopters, including support for it by default since Fedora Core 2. Other distributions include support for it such as Debian as of version 9 Stretch release and Ubuntu as of 8.04 Hardy Heron. As of version 11.1, openSUSE contains SELinux "basic enablement". SUSE Linux Enterprise 11 features SELinux as a "technology preview".

SELinux is popular in systems based on linux containers, such as CoreOS Container Linux and rkt. It is useful as an additional security control to help further enforce isolation between deployed containers and their host.

SELinux is available since 2005 as part of Red Hat Enterprise Linux (RHEL) version 4 and all future releases. This presence is also reflected in corresponding versions of derived systems such as CentOS, Scientific Linux, AlmaLinux and Rocky Linux. The supported policy in RHEL4 is targeted policy which aims for maximum ease of use and thus is not as restrictive as it might be. Future versions of RHEL are planned to have more targets in the targeted policy which will mean more restrictive policies.

**Use case scenarios**

SELinux can potentially control which activities a system allows each user, process, and daemon, with very precise specifications. It is used to confine daemons such as database engines or web servers that have clearly defined data access and activity rights. This limits potential harm from a confined daemon that becomes compromised.

Command-line utilities include: `chcon`, `restorecon`, `restorecond`, `runcon`, `secon`, fixfiles, setfiles, load_policy, booleans, getsebool, setsebool, togglesebool, setenforce, semodule, postfix-nochroot, check-selinux-installation, semodule_package, `checkmodule`, selinux-config-enforcing, selinuxenabled, and selinux-policy-upgrade.

To have them, we have to install in our linux, for example, the following is to install them in ubuntu,

![selinux_tool](../../../images/linux_administration/selinux_tool.png)

**Examples**

* To put SELinux into enforcing mode:

`setenforce 1`

You will see the following output if you run it,

```shell
xiaofengli@xiaofenglx:~$ setenforce 1
setenforce: SELinux is disabled
```

* To query the SELinux status:

`getenforce`

```shell
xiaofengli@xiaofenglx:~$ getenforce
Disabled
```

## Ref

- https://en.wikipedia.org/wiki/Security-Enhanced_Linux#:~:text=Security%2DEnhanced%20Linux%20(SELinux),mandatory%20access%20controls%20(MAC).

- https://github.blog/developer-skills/programming-languages-and-frameworks/introduction-to-selinux/

- https://opensourcewatch.beehiiv.com/p/everything-wanted-know-selinux-afraid-run

- https://wiki.centos.org/HowTos(2f)SELinux.html

- https://docs.fedoraproject.org/en-US/quick-docs/selinux-getting-started/