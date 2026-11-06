# SSH

```shell
xiaofengli@xiaofenglx:~/git/localhost$ GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_webbertech" git push
Enumerating objects: 24, done.
Counting objects: 100% (24/24), done.
Delta compression using up to 4 threads
Compressing objects: 100% (16/16), done.
Writing objects: 100% (16/16), 2.40 MiB | 8.28 MiB/s, done.
Total 16 (delta 5), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (5/5), completed with 5 local objects.
To github.com:kevinli-webbertech/localhost.git
   883002b..e059872  main -> main
```

To craft it into your shell script, and put it into your `~/.bash_profile`,

* Open your `~/.bash_profile`, add the following function at the bottom of the file,

```shell
function set_ssh_private_key() {
 if [[ $1 = "webbertech" ]]; then
    GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_webbertech"
 elif [[ $1 = "tekfive" ]]; then
    GIT_SSH_COMMAND="ssh -i ~/.ssh/id_rsa_tekfive"

 elif [[ $1 = "-h" || $1 == "--help" ]]; then
    echo "possible values are: webbertech or tekfive"
 else
    echo "type -h or --help for help menu" 
 fi
 echo "your github configuratin has been set to:"
 echo $GIT_SSH_COMMAND
}
```

* add the following line to rename the function name to something else,

`alias git_config=set_ssh_private_key`

* execute the `./bash_profile` otherwise it will not take effect,

`source ~/.bash_profile`

### Ref

`git config core.sshCommand "ssh -i /path/to/your/private_key"`

https://www.baeldung.com/linux/ssh-private-key-git-command