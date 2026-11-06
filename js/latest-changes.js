(function () {
  'use strict';
  const endpoint = 'https://api.github.com/repos/kevinli-webbertech/kevinli-webbertech.github.io/commits?sha=main&per_page=5';
  function render(list, commits) {
    list.replaceChildren();
    commits.forEach(function (commit) {
      const item = document.createElement('li');
      const link = document.createElement('a');
      link.href = 'https://github.com/kevinli-webbertech/kevinli-webbertech.github.io/commit/' + encodeURIComponent(commit.sha);
      link.target = '_blank';
      link.rel = 'noopener noreferrer';
      link.textContent = commit.message;
      const time = document.createElement('time');
      time.dateTime = commit.date;
      time.textContent = ' — ' + new Date(commit.date).toLocaleDateString();
      item.append(link, time);
      list.append(item);
    });
  }
  const popupSessionKey = 'latest-changes-popup-shown';
  function hasShownPopup() {
    try { return window.sessionStorage.getItem(popupSessionKey) === '1'; }
    catch (_) { return false; }
  }
  async function init() {
    const noticeList = document.getElementById('latest-git-changes');
    let popupList;
    if (window.self === window.top && !noticeList && !hasShownPopup()) {
      const dialog = document.createElement('dialog');
      dialog.className = 'latest-changes-dialog';
      dialog.setAttribute('aria-labelledby', 'latest-changes-title');
      const title = document.createElement('h2');
      title.id = 'latest-changes-title';
      title.textContent = 'Latest website changes';
      popupList = document.createElement('ul');
      popupList.innerHTML = '<li>Loading latest changes…</li>';
      const form = document.createElement('form');
      form.method = 'dialog';
      const button = document.createElement('button');
      button.type = 'submit';
      button.textContent = 'Confirm and close';
      form.append(button);
      dialog.append(title, popupList, form);
      document.body.append(dialog);
      dialog.showModal();
      try { window.sessionStorage.setItem(popupSessionKey, '1'); }
      catch (_) { /* Storage may be disabled by browser settings. */ }
    }
    if (!noticeList && !popupList) return;
    function update(commits) {
      [noticeList, popupList].filter(Boolean).forEach(list => render(list, commits));
    }
    // Display the saved copy even when GitHub is unavailable or rate limited.
    try {
      const saved = await fetch('js/latest-changes.json');
      if (!saved.ok) throw new Error('Saved changes unavailable');
      update(await saved.json());
    } catch (_) {
      [noticeList, popupList].filter(Boolean).forEach(list => {
        list.textContent = 'Latest changes are temporarily unavailable.';
      });
    }
    try {
      const response = await fetch(endpoint, { headers: { Accept: 'application/vnd.github+json' } });
      if (!response.ok) return;
      const commits = await response.json();
      update(commits.map(item => ({
        sha: item.sha,
        date: item.commit.committer.date,
        message: item.commit.message.split('\n')[0]
      })));
    } catch (_) { /* Keep the saved copy. */ }
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', init);
  else init();
}());
