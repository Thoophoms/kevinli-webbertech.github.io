# `codeql-config.yml`

To specify a `codeql-config.yml` file in your GitHub workflow, you need to configure the CodeQL analysis action (`github/codeql-action`) to use the custom configuration file. The `codeql-config.yml` file is used to customize how CodeQL analyzes your code, such as specifying queries to run, paths to include/exclude, and other analysis settings.

Here’s how you can integrate `codeql-config.yml` into your GitHub workflow:

---

### Steps to Specify `codeql-config.yml`

1. **Create the `codeql-config.yml` File**:
   - Place the `codeql-config.yml` file in your repository, typically in the `.github/codeql/` directory (or another location of your choice).
   - Example `codeql-config.yml`:

     ```yaml
     name: "Custom CodeQL Configuration"

     queries:
       - uses: security-and-quality
     paths:
       - include: src/
       - exclude: tests/
     ```

2. **Update Your GitHub Workflow**:
   - Modify your workflow file (e.g., `.github/workflows/codeql-analysis.yml`) to reference the `codeql-config.yml` file using the `config-file` parameter of the `github/codeql-action/init` action.

   Example workflow:

   ```yaml
   name: "CodeQL Analysis"

   on:
     push:
       branches: [main]
     pull_request:
       branches: [main]
     schedule:
       - cron: '0 0 * * 0' # Weekly schedule

   jobs:
     analyze:
       name: Analyze
       runs-on: ubuntu-latest

       steps:
         - name: Checkout repository
           uses: actions/checkout@v4

         - name: Initialize CodeQL
           uses: github/codeql-action/init@v3
           with:
             languages: javascript # Specify the language(s) to analyze
             config-file: .github/codeql/codeql-config.yml # Path to your config file

         - name: Perform CodeQL Analysis
           uses: github/codeql-action/analyze@v3
   ```

---

### Explanation of the Workflow

1. **Trigger Events**:
   - The workflow runs on `push` to the `main` branch, `pull_request` to the `main` branch, and on a weekly schedule.

2. **Jobs**:
   - A single job named `analyze` runs on the `ubuntu-latest` runner.

3. **Steps**:
   - **Checkout repository**: Clones the repository using `actions/checkout`.
   - **Initialize CodeQL**: Initializes the CodeQL analysis using the `github/codeql-action/init` action. The `config-file` parameter specifies the path to the `codeql-config.yml` file.
   - **Perform CodeQL Analysis**: Runs the CodeQL analysis using the `github/codeql-action/analyze` action.

---

### Example `codeql-config.yml` File

Here’s an example of what your `codeql-config.yml` file might look like:

```yaml
name: "Custom CodeQL Configuration"

# Specify queries to run
queries:
  - uses: security-and-quality # Use the default security and quality queries
  - name: custom-queries/example.ql # Include a custom query

# Specify paths to include/exclude
paths:
  - include: src/ # Analyze files in the src directory
  - exclude: tests/ # Exclude files in the tests directory
```

---

### Key Parameters in `codeql-config.yml`

1. **`queries`**:
   - Specify the queries to run during the analysis.
   - You can use pre-defined query suites (e.g., `security-and-quality`) or custom queries.

2. **`paths`**:
   - Define which files or directories to include or exclude from the analysis.

3. **`languages`**:
   - Specify the languages to analyze (if not already defined in the workflow file).

4. **`packs`**:
   - Include CodeQL packs for additional query suites or custom analysis.

---

### Advanced Configuration

If you need to analyze multiple languages or use additional configurations, you can extend the `codeql-config.yml` file and workflow. For example:

```yaml
name: "Multi-Language CodeQL Configuration"

queries:
  - uses: security-and-quality

paths:
  - include: src/
  - exclude: tests/

languages:
  - javascript
  - python
```

In the workflow, you can specify the languages in the `init` step:

```yaml
- name: Initialize CodeQL
  uses: github/codeql-action/init@v3
  with:
    languages: javascript, python
    config-file: .github/codeql/codeql-config.yml
```

---

### Best Practices

1. **Place Configuration in a Standard Location**:
   - Store the `codeql-config.yml` file in `.github/codeql/` for consistency.

2. **Test Your Configuration**:
   - Run the workflow locally or in a test branch to ensure the configuration works as expected.

3. **Use Query Suites**:
   - Leverage pre-defined query suites like `security-and-quality` to cover common vulnerabilities and code quality issues.

4. **Exclude Non-Relevant Files**:
   - Use the `paths` parameter to exclude directories like `tests/` or `node_modules/` to speed up analysis.

By following these steps, you can effectively integrate a `codeql-config.yml` file into your GitHub workflow and customize CodeQL analysis for your project.