Task 1: Figure out a NPM tool to uglify our js for production, generate a dist/js folder, and we replace the path to point to that encrypted js and to help encrypt the website.

What Are We Doing?

- We’re taking your JavaScript code and making it smaller (minifying it) to make your website load faster.
- The smaller files will be stored in a folder called dist/js.
- We will then tell your website to use these smaller, encrypted (minified) files instead of the original ones.

Before we start, if you're using MacOs then you need to make sure all requirements are there, or you will get an error.

Step 1: Update Homebrew
Homebrew is a package manager for macOS, and it likely manages the missing library. Update it to ensure everything is current:

in a bash command:
`brew update`

Step 2: Reinstall ICU4C
Reinstall the ICU library to make sure it's correctly installed:

bash
`brew reinstall icu4c`

Step 3: Link ICU4C
Ensure the library is correctly linked so Node.js can find it:

bash
`brew link icu4c --force`

Step 4: Reinstall Node.js
Your Node.js installation might also need updating or fixing. Reinstall it with Homebrew:

1. Uninstall Node.js:

bash
`brew uninstall node`

2. Install Node.js again:

bash
`brew install node`

3. Confirm Node.js is installed:

bash
`node -v

npm -v`


Now, we will start with the Uglifying process:

Step 1: Install a Tool for Minifying JavaScript

We need a tool to shrink your JavaScript files. There are two popular tools:

- Terser (better for modern JavaScript)
- UglifyJS (good but not as modern)

To install one of these tools:

- Open your terminal or command prompt.
- Type the following command and press Enter:

For Terser:

bash
`npm install terser --save-dev`

For UglifyJS:

bash
`npm install uglify-js --save-dev`

This downloads the tool and adds it to your project.

Step 2: Create a Folder for the Minified Files

You need a place to store the minified (shrunken) JavaScript files. Let’s create a folder called dist/js:

1. In your terminal, type: `mkdir -p dist/js`
2. This will create a folder called dist with a subfolder called js.

Step 3: Write a Script to Minify JavaScript

To shrink your JavaScript files, we’ll write a script in your package.json file. The package.json file is where you store project settings and scripts.

1. Open the package.json file in your project folder.
2. Add the following under the "scripts" section:

For UglifyJS:

json
`{
  "name": "javascript-warmup",
  "version": "1.0.0",
  "scripts": {
    "uglify-js": "terser src/js/*.js --compress --mangle --output dist/js/bundle.min.js"
  },
  "devDependencies": {
    "terser": "^5.10.0"
  }
}
`

This tells your project how to shrink all .js files in the src/js folder and save the uglified files in dist/js.

Step 4: Update Your Website to Use the uglified JavaScript

After creating the smaller files, you need to tell your website to use them.

1. Open your HTML file.
2. Find the line where your JavaScript is included, like this:

html
`<script src="src/js/content_locker.js"></script>`

3. Change it to:

html
`<script src="https://kevinli-webbertech.github.io/dist/js/bundle.min.js"></script>`

This tells the website to use the uglified version of the JavaScript file.

The project directory should look something like this:

kevinli-webbertech.github.io/
│

├── package.json

├── src/

│   └── js/

│           └── content_locker.js

└── dist/

└── js/


Step 5: Run the uglified Script

Now, let’s uglify the JavaScript files:

1. In the terminal, type:

bash
`npm run uglify-js`

2. Press Enter. 

The tool will process your JavaScript files and save the uglified versions in the dist/js folder.

**Task 2: use setTimer and pick one html file such as git.html and mimic medium.com feature, where we allow users to read for 15 secs article and then it will pop up that modal dialog box.**

What is HTML?

HTML (HyperText Markup Language) is used to create the structure of a webpage.

What we’re doing:

We’re creating an HTML file (git.html) that contains the article content and a modal pop-up that will appear after 15 seconds.

Key parts of the HTML file:

Article Content:

This is the part users will read (for example, an article about Git).
Modal:

The modal is a pop-up box that will show a message like "Subscribe to Continue."

Steps to implement Task2:

1. HTML file setup:

- Create a file (git.html)
- Add a modal structure to the HTML that will display the pop-up after 15 seconds.

2. CSS for Modal:

Add basic styles to make the modal look visually appealing in the (style.css) and link it to the html file.

3. JavaScript to Control Timer and Modal:

as in the logic in the file modal-timer.js

**Task 3: We have a python backend service already and we will deploy it to our AWS. I will work with you in a zoom.**

Step 1: Fix Your Local Python Environment

Follow the earlier recommendation to set up a virtual environment to handle dependencies safely.

1. Create a Virtual Environment:

bash
`python3 -m venv venv`

2. Activate the Virtual Environment:

bash
`source venv/bin/activate`

3. Install Required Packages: Assuming your project has a requirements.txt file:

bash
`pip install -r requirements.txt`

If no requirements.txt exists, install your backend dependencies manually (e.g., Flask):

bash
`pip install flask`

4. Verify Local Functionality: Test the backend service locally by running:

bash
`python course_authentication.py`

Step 2: Prepare for AWS Deployment

1. Generate requirements.txt: Export all installed dependencies:

bash
`pip freeze > requirements.txt`

2. Containerize Your Backend (Optional): Use Docker if your deployment process involves containers:

Create a Dockerfile in your project directory:
dockerfile

`FROM python:3.9-slim
WORKDIR /app
COPY . /app
RUN pip install --no-cache-dir -r requirements.txt
CMD ["python", "course_authentication.py"]`

3. Build and test the image locally:

bash

`docker build -t my-backend-service .`
`docker run -p 5000:5000 my-backend-service`

