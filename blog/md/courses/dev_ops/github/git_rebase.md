`git rebase` is a powerful Git command used to integrate changes from one branch into another by reapplying commits on top of another base branch. It is often used to maintain a clean, linear project history. Here's a breakdown of how it works and when to use it:

---

### **What Does `git rebase` Do?**

1. **Reapplies Commits**: It takes the commits from your current branch and reapplies them on top of the latest commit of another branch (usually the main branch).
2. **Creates New Commits**: During the rebase, Git creates new commits for each of the original commits, even if the content remains the same.
3. **Linear History**: It results in a linear project history, making it easier to understand the sequence of changes.

---

### **Basic Syntax**
```bash
git rebase <base-branch>
```
- `<base-branch>`: The branch you want to rebase onto (e.g., `main`, `develop`).

---

### **Common Use Cases**

1. **Updating a Feature Branch**:
   - If the `main` branch has been updated, you can rebase your feature branch to include the latest changes from `main`.
   ```bash
   git checkout feature-branch
   git rebase main
   ```

2. **Cleaning Up Commit History**:
   - Use `git rebase -i` (interactive rebase) to squash, edit, or reorder commits.
   ```bash
   git rebase -i HEAD~3  # Rebase the last 3 commits
   ```

3. **Resolving Conflicts**:
   - If conflicts occur during a rebase, Git will pause and allow you to resolve them. After resolving conflicts, use:
   ```bash
   git rebase --continue
   ```

4. **Aborting a Rebase**:
   - If something goes wrong, you can abort the rebase and return to the original state:
   ```bash
   git rebase --abort
   ```

---

### **Interactive Rebase**

Interactive rebase allows you to modify commits during the rebase process. Common commands in the interactive rebase editor include:
- `pick`: Use the commit as-is.
- `squash`: Combine the commit with the previous one.
- `edit`: Pause to amend the commit.
- `drop`: Remove the commit entirely.

Example:
```bash
git rebase -i HEAD~5  # Rebase the last 5 commits interactively
```

---

### **Rebase vs. Merge**

- **Rebase**:
  - Creates a linear history.
  - Rewrites commit history (new commit hashes).
  - Best for cleaning up history before merging.

- **Merge**:
  - Preserves the original commit history.
  - Creates a merge commit.
  - Best for integrating completed features.

---

### **Best Practices**

1. **Avoid Rebasing Public Commits**:
   - Rebasing rewrites commit history, which can cause issues for collaborators if the commits have already been pushed to a shared repository.
2. **Rebase Locally**:
   - Use rebase for local branches to clean up history before pushing.
3. **Communicate with Your Team**:
   - Ensure everyone is aware of rebasing practices to avoid conflicts.

---

### **Example Workflow**

1. Start a new feature branch:
   ```bash
   git checkout -b feature-branch
   ```

2. Make some commits on the feature branch.

3. Update the `main` branch:
   ```bash
   git checkout main
   git pull origin main
   ```

4. Rebase the feature branch onto `main`:
   ```bash
   git checkout feature-branch
   git rebase main
   ```

5. Resolve any conflicts and continue:
   ```bash
   git rebase --continue
   ```

6. Push the rebased branch:
   ```bash
   git push origin feature-branch --force-with-lease
   ```

---

Let me know if you need further clarification or examples!