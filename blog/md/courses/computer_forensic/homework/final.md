# Final Project - Self-signed Certificate

**Problem Statement**

>Hint: This section is to give you some IT background of some problem we need to address.

For instance, let us assume that you have a python flask API http server running and say your domain is http://abc.com/students/all, normally it will return things like json, such as,

```json
{
  {“id”: 1, “first_name”: “Damian”, “last_name”: “Rusek”},
  {“id”: 2, “first_name”: “John”, “last_name”: “Kapp”}
}
```

The problem now is that, if you JS and html are hosted on a site that is secured with `https`, such as, https://a.com/, and it calls an api by doing this,

`fetch(“http://b.com/students/all”)`,

and it will fail. Because **it is from https to call http, which is not allowed**.

**Solution**

Let us say we have a EC2 VM that runs the python web service and host an API `https://b.com/students/all` in the EC2 VM of `b.com`.

And we would like to ssh to the EC2 VM of `b.com` and set up something called a self-signed certificate. And we will have to do this and test it with curl commands.

In this project we need to learn what is CA, what is certificate and how the private and public key works in the sense of https. And how to set it up, using AWS’s cert manager or just use some opensource project by self-signed certificate.

**Requirements and Scoring**

* Set up a VM that mimic let us call it `b` and we use `b` or `b.com` interchanbly here. We do not need a real domain, so you do not need to spend money to buy one. Just the DNS provided by AWS. For gaining public IP and make it more flexible you could use the Elastic IP but it is not necessary. (20 points)

* You could ssh to the b.com. And do the `apt install` of `vim` or neccessary ssh related software to set up a self-signed certificate. (20 points)

* You must provide a word document and explain step by step what it is and show the real image of your setup not something from the internet. This step of prove the autheneticity of the ownership of your work and not others are essential. (20 points)

* You would need to use googling or Chatgpt to make sure that you run a http server for python or Java projects, that renders the following API, and JSON output,

**API**: `http://b.com/students/all`

**JSON**: Json output like the following,

```json
{
  {“id”: 1, “first_name”: “Damian”, “last_name”: “Rusek”},
  {“id”: 2, “first_name”: “John”, “last_name”: “Kapp”}
}
```

(This is 20 pts).

* Use `curl` or `postman` to call the https to confirm that your `https` API setup is done. (20 pts)

>Hint: If you use Google GCP it is also fine. But you need to take some screenshots to prove your setup.
