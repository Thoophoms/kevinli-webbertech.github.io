# midterm - CodeQL Scanning

* Installation of the CodeQL (20 pts)

https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli

* Preparing your code for CodeQL analysis (20 pts)

https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/setting-up-the-codeql-cli

* Checkout a report and do the CodeQL Scanning. (60 pts)

https://docs.github.com/en/code-security/codeql-cli/getting-started-with-the-codeql-cli/analyzing-your-code-with-codeql-queries

```commandline
codeql database analyze /codeql-dbs/example-repo \
    javascript-code-scanning.qls --sarif-category=javascript-typescript \
    --format=sarif-latest --output=/temp/example-repo-js.sarif
```

In your homework you should upload a word file and a `sarif` file.

For more information, I have a CodeQL scanning tutorial on my website.