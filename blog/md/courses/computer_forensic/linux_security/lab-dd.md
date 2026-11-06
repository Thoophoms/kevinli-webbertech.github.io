# lab - using dd command

In this lab, we will do the following two things,

* know how to use dd command to dump core memory (this is one of the usage of dd commands and probably one of the safest that we can try in our computer).

* know how to use hexeditor to read on binary file.

## Step 1 using `root` to dump core memory about 2M to a bin file in your `/tmp`

`sudo dd if=/proc/kcore of=/tmp/memory.bin bs=1M count=2`

## Step 2 using `hexedit` to view the binary file

**Example1**

```shell
xiaofengli@xiaofenglx:/$ sudo dd if=~/Desktop/data-analysis2.jpg of=/dev/sdc1 bs=512 count=1000
75+1 records in
75+1 records out
38669 bytes (39 kB, 38 KiB) copied, 0.000292738 s, 132 MB/s
```

**Example 2**

```shell
xiaofengli@xiaofenglx:/$ sudo dd if=/proc/kcore of=/tmp/memory.bin bs=1M count=2
2+0 records in
2+0 records out
2097152 bytes (2.1 MB, 2.0 MiB) copied, 0.00162996 s, 1.3 GB/s
xiaofengli@xiaofenglx:/$ cd /tmp
xiaofengli@xiaofenglx:/tmp$ ls memory.bin 
memory.bin
xiaofengli@xiaofenglx:/tmp$ ls -al memory.bin 
-rw-r--r-- 1 root root 2097152 Feb  5 23:55 memory.bin
xiaofengli@xiaofenglx:/tmp$ chmod +x memory.bin 
chmod: changing permissions of 'memory.bin': Operation not permitted
xiaofengli@xiaofenglx:/tmp$ sudo chmod +x memory.bin 
xiaofengli@xiaofenglx:/tmp$ hexedit memory.bin 
```
