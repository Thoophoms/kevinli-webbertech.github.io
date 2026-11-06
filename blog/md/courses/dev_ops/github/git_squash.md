To perform a **squash merge** in Git via the command line, follow these steps:

### **1. Checkout the Target Branch (e.g., `main` or `develop`)**
```sh
git checkout main  # or your target branch
```

### **2. Merge the Feature Branch with Squash**
```sh
git merge --squash feature-branch
```
This prepares all commits from `feature-branch` to be squashed into a single commit without automatically creating the commit.

### **3. Commit the Squashed Changes**
```sh
git commit -m "A single commit message summarizing the changes"
```
This will combine all the changes into a single commit.

### **4. Push the Changes**
```sh
git push origin main
```

---

### **Alternative: Interactive Rebase (for Local Branch)**
If you want to squash commits within a branch before merging:

1. **Checkout the feature branch**  
   ```sh
   git checkout feature-branch
   ```

2. **Rebase interactively**  
   ```sh
   git rebase -i HEAD~N
   ```
   *(Replace `N` with the number of commits you want to squash.)*

3. **In the editor:**
   - Change `pick` to `squash (s)` for all but the first commit.
   - Save and exit.

4. **Push the changes (force push if already pushed earlier)**  
   ```sh
   git push origin feature-branch --force
   ```

Would you like a specific workflow tailored to your setup? 🚀