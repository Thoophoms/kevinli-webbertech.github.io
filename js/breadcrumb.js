(function () {
  function labelize(segment) {
    return decodeURIComponent(segment)
      .replace(/[-_]+/g, " ")
      .replace(/\b\w/g, (c) => c.toUpperCase());
  }

  function getCrumbHref(acc) {
    return acc === "/blog" ? "/blog.html" : null;
  }

  function buildBreadcrumb() {
    const nav = document.querySelector("#breadcrumb") || document.querySelector("[data-breadcrumb]");
    if (!nav) return;

    const path = window.location.pathname
      .replace(/\/+/g, "/")
      .replace(/index\.html$/i, "")
      .replace(/\.html$/i, "");

    const parts = path.split("/").filter(Boolean);
    if (!parts.length) return;

    nav.style.cssText = "display:flex; align-items:center; flex-wrap:wrap; gap:6px; font-size:0.9rem; padding:8px 0; margin-bottom:12px;";

    const items = [];
    let acc = "";

    items.push('<a href="/index.html" style="text-decoration:none; color:#0366d6;">Home</a>');

    for (let i = 0; i < parts.length; i++) {
      acc += "/" + parts[i];
      if (parts[i] === "html" && (i === 0 || parts[i - 1] === "blog")) continue;

      const isLast = i === parts.length - 1;
      const text = labelize(parts[i]);

      if (isLast) {
        items.push(`<span style="color:#555; font-weight:600;">${text}</span>`);
      } else {
        const crumbHref = getCrumbHref(acc);
        if (crumbHref) {
          items.push(`<a href="${crumbHref}" style="text-decoration:none; color:#0366d6;">${text}</a>`);
        } else {
          items.push(`<span style="color:#555;">${text}</span>`);
        }
      }
    }

    nav.innerHTML = items.join(' <span style="color:#999;">&gt;</span> ');
  }

  document.addEventListener("DOMContentLoaded", buildBreadcrumb);
})();