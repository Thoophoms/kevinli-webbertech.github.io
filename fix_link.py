from pathlib import Path

tag = '<script src="https://kevinli-webbertech.github.io/js/breadcrumb.js" defer></script>\n'
root = Path("blog/html")

for f in root.rglob("*.html"):
    text = f.read_text(encoding="utf-8")
    if "https://kevinli-webbertech.github.io/js/breadcrumb.js" in text:
        continue

    if "</body>" in text:
        text = text.replace("</body>", f"{tag}</body>")
    elif "</head>" in text:
        text = text.replace("</head>", f"{tag}</head>")
    else:
        text += "\n" + tag

    f.write_text(text, encoding="utf-8")
    print(f"updated: {f}")
