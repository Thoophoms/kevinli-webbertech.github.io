# HW6 Jenkins + Github Public Repo

Please include the original questions in your homework report. Please check out of syllabus for details or you will lose points.

1. Please follow the link below, and try to run the dockerized Jenkins. (25 pts)

https://www.jenkins.io/doc/book/installing/docker/

Please prove that your Jenkins instance is running successfully inside of a container and it is ready to be used.

2. Jenkins Integration with Github. (25 pts)

* Prepare a nodejs project and commit to your github as a public-access repo,

https://medium.com/@mudasirhaji/complete-step-by-step-jenkins-cicd-with-github-integration-aae3961b6e33

* Please prove that you can build a Jenkins job from a github and build the final artifact.

3. Please provide ssh solutions to add public key to your github account. (25 pts)

Using ssh public-private key can help you work with github without a password and it will grant you access. Please provide details solutions how to do that.

4. Please explain the relationship between public and private keys.

   * How they were related and being used in the SSL/TLS? (hint: algorithm) (10 pts)
   * When you have two github accounts and two repos but you want to commit codes to two different repos under two different github accounts in the same linux machine. How would you manage two pairs of private key and public keys. (hint: ~/.ssh/config and other solutions) (15 pts)