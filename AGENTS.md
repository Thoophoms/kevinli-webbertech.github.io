# Website maintenance

- Keep changes scoped to the requested work and preserve existing local edits.
- The Featured Classes default view in `blog.html` shows 14 cards before Load more.
- `notices.html` and the page-load popup share `js/latest-changes.js`. It displays the latest five commit subjects from the public repository main branch, with `js/latest-changes.json` as a fallback.
- Before completing website changes, run `node scripts/generate-notices.cjs` to refresh the saved commit messages. The saved copy reflects existing commits; the live GitHub feed includes new commits after they are pushed.
- Keep the popup on both `index.html` and `blog.html`, shown on every top-level page load. Keep a keyboard-accessible Confirm and close button; never show a second popup inside the Notices iframe.
- Validate changed JavaScript with `node --check` and run `git diff --check`.
- Commit and push only when the user authorizes it.
