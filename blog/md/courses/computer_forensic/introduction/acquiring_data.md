# AQUIRING DATA

### **Data acquisition approaches**

After taking essential precautions to preserve your evidence, you're finally ready to acquire your data. There are many ways of acquiring data in computer forensics. Static acquisition is one of the most basic and common data acquisition methods. Static acquisition retrieves data from non-volatile sources, such as a hard drive or USB drive. In a non-volatile source, data remains on the storage device after turning the power off. Live acquisition is becoming more necessary these days because of encryption. Live acquisition acquires data from a volatile source, such as main memory, also known as random access memory, or RAM. In a volatile source, data goes away from the storage device after it's turned off. In addition to static and live acquisition types, there is another way of acquisition, which is remote acquisition. Remote acquisition is done through a network connection and involves a client-server architecture. You often install a client on a machine from which you want to retrieve the data. The current trend is that live and remote acquisition practices are becoming more prevalent due to the encryption challenges I mentioned earlier. Static acquisition is more difficult, especially these days, because a data drive gets encrypted when a computing device is inactive. This means, by the time you're trying to do static acquisition, all you can get is an encrypted version of the data you're seeking.]

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/data-acquisition-approaches?autoSkip=true&resume=false&u=56745521#)


### **Static acquisition with open-source tools**

There are plenty of open-source utilities out there you can use to get an image of a drive. We'll use an open-source tool called dd to get an image of a USB drive. Our goal here is to get an image of an entire physical drive rather than a partition on the physical drive. Therefore, we'll be using /dev/sdb instead of /dev/sdb1 to refer to our USB drive. We've already looked at finding out how a USB drive is recognized in a file system on Linux. The command to use for our imaging task is very simple. Type sudo, space, dd, space, if. IF here stands for input file. Equal sign, forward slash, dev, forward slash, sdb, instead of sdb1, which is a partition. Next, type a space, and then of, equals sign. OF here stands for output file. After the equal sign, type the target file name of the image. Let's use dot, forward slash, usb, underscore, image. The dot here stands for the current directory. And then the extension dot dd. Press enter. Because you're using sudo, it's asking for the password. I type the password, and I'm pressing enter. The imaging process just started, and until it's done, your command prompt won't return. One way of checking whether the file has been actually created is to open another terminal window to see the name of the file showing up in your directory. Go to file, choose new window. Type ls and then press enter. As you can see, the file has been created. This file will be getting bigger and bigger as the imaging process is being done. Now, I'll type ls, space, dash l to list some more details of the file. Press enter. This is the file size. Let's try ls dash l again. Press enter. As you can see, compared to the previous file size, it's getting bigger. This means that the imaging process is going on successfully. dd is one of the most basic tools out there you can use to get your simple imaging task done, but there are also more advanced tools for the imaging task you can use to make your job as a computer forensics investigator a little easier. One of these tools is dcfldd, a forensic version of dd.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/static-acquisition-with-open-source-tools?resume=false&u=56745521#)

### **Static acquisition case study with dd**

There's also a way to split your image file into multiple fragments. Fragmentation is sometimes necessary because you have to put the files on media with very limited capacities. To do this, we can use dd together with another Linux utility. Type sudo space dd space input file equals sign forward slash dev forward slash sdb. which is the physical USB drive connected to my computer, and type space. Instead of typing OF, or output file and then equals sign target file name here, we'll use something called a filter. A filter in Linux takes the output of a previous command and passes that output as an input to the next command. Whatever the dd input file command produces, its output will go to the following command as an input. In this case, the output sent as an input will be the image file, but we'll split it into multiple files. The command we need for this is split. The split file size of my choice is 650 megabytes. That's why we type pipe here, space split space dash b space 650m space dash space usbimage dot. Whatever comes after the dot will serve as an extension so that when the files are created, they'll begin with the file name usbimage dot and extension. The file extension will be different in a sequential order to reflect the fact that a single image file is now split into multiple files. Press enter. The imaging process has begun. While it's getting done, we can see the progress in the second window. Type ls, press enter. So far there have been four files created: usbimage.aa, usbimage.ab, usbimage.ac, usbimage.ad. There'll be some more files coming after this. By learning about these additional options for imaging, you have more flexibility in dealing with whatever situation is thrown at you.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/static-acquisition-case-study-with-dd?resume=false&u=56745521#)

### **Static acquisition case study with dcfldd**

The imaging process is finally over. Let's check the usbimage.log file. To see the content of this file, We'll be using the more command. Type more and the name of the log file. usb image.log. Please note that there was a typo. So it's i-a-m-g-e.l-o-g instead of i-m-a-g-e.l-o-g. But it still works. Press Enter. As you can see, the md5 hash value of your image is now showing. Let's also check whether the image file has been created. Type ls, press Enter, and you can see the usbimage.dd file with the correct spelling. As you can tell, dcfldd has more computer forensics features compared to dd. Plus, it's easier to use. Although the dcfldd software is free, you may still have to install it to your favorite Linux distribution. If you want to learn more about dcfldd, please check out this website.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/static-acquisition-case-study-with-dcfldd?resume=false&u=56745521#)

### **Live acquisition case study with a commercial tool**

FTK Imager can serve as a live acquisition tool too. Here is how you do it. Go to file, choose capture memory. You have to specify what is your destination path. Next, click on browse. Let's make our destination folder as our desktop. Click OK, and then click on capture memory. The memory capturing process has been finished successfully. Click on close. You can see the memory dump file named memdump.mem.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/live-acquisition-case-study-with-a-commercial-tool?resume=false&u=56745521#)

### **Challenge: Live acquisition with a memory dump file**

To analyze the result of your live acquisition, you still need a separate software program. The software tool can be as simple as a hex editor. In this challenge, open the memory dump file in a hex editor and try to see what's inside. Do a search to find sensitive information.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/challenge-live-acquisition-with-a-memory-dump-file?resume=false&u=56745521#)

### **Solution: Live acquisition with a memory dump file**

Let's open Neo. Go to file, open, open file. Choose mamdump.mam. Click open. Let's do a search. Click on the find icon. Make sure string is chosen and type password. Click find. As you can see, you can find every occurrence of the word password in your entire memory dump file like this, and you can keep going.

- (https://www.linkedin.com/learning/cybersecurity-foundations-computer-forensics/solution-live-acquisition-with-a-memory-dump-file?resume=false&u=56745521#)