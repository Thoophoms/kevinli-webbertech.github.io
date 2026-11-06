(function () {
  var bookmarkPromptKey = 'bookmarkPromptShownAt';
  var promptCooldownMs = 7 * 24 * 60 * 60 * 1000;

  function getStorage() {
    try {
      return window.localStorage;
    } catch (error) {
      return null;
    }
  }

  var storage = getStorage();
  if (storage) {
    var lastShownAtRaw = storage.getItem(bookmarkPromptKey);
    var lastShownAt = Number(lastShownAtRaw);
    if (Number.isFinite(lastShownAt) && Date.now() - lastShownAt < promptCooldownMs) {
      return;
    }
  }

  var isMac = navigator.platform.toUpperCase().indexOf('MAC') >= 0;
  var shortcut = isMac ? 'Command (⌘) + D' : 'Ctrl + D';
  var shouldShowTip = confirm('Enjoying WebberTech? Click OK to see how to bookmark this site to your browser bar.');

  if (shouldShowTip) {
    alert('To bookmark this website to your browser bar, press ' + shortcut + ' now.');
  }

  if (storage) {
    storage.setItem(bookmarkPromptKey, String(Date.now()));
  }
})();
