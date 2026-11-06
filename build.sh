#!/bin/bash

'''
Step 1. We already have the package.json file, so just do a `npm install`.

(base) xiaofengli@xiaofenglx:~/git/kevinli-webbertech.github.io$ npm install

added 12 packages, and audited 13 packages in 5s

found 0 vulnerabilities

Step 2 modify package.json and make sure that it only modify the content_locker.js and minify it.

Step 3  `npm run uglify-js`
'''

# write a if to make sure that we create the dist/js dir

npm install
npm run uglify-js

