# Troubleshooting for docker running in Apple M* Chip Macs

The target audiences of this article are Mac M*  Chip Users. M1 and M2 are Apple’s chip and it is currently having issues with docker. Please follow the steps below to fix the problems on your computer.

1/ Install colima using homebrew,

`brew install colima`

After installation, you could check where it is installed,

```
kevins-Laptop:~ kevinli$ which colima
/opt/homebrew/bin/colima
```

2/ Run Colima to emulate it is x64 architecture

I had a script called Colima.sh in my ~/ directory,

```
#!/bin/bash
colima start --arch x86_64 --memory 4
```

or you just copy the line `colima start --arch x86_64 --memory 4` and run it. It will take a little while to start.

3/ Test docker is good

And then type

`docker --help`

If everything all good, then run the following,

4/ Test run with Hadoop image

Then run the following,
`
docker run -it sequenceiq/hadoop-docker:2.7.0 /etc/bootstrap.sh -bash
`
Make sure you use docker commands to check the container is running not shutdown instantly after this.
