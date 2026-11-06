"""One-off utility: render a course lab Markdown file to a styled PDF.

Usage: python md_to_pdf.py <input.md> <output.pdf>
"""
import sys
import markdown
from xhtml2pdf import pisa

STYLE = """
<style>
  body { font-family: Helvetica, Arial, sans-serif; font-size: 11pt; line-height: 1.4; }
  h1 { font-size: 20pt; color: #1a1a1a; border-bottom: 2px solid #333; padding-bottom: 6px; }
  h2 { font-size: 15pt; color: #222; margin-top: 18px; }
  h3 { font-size: 13pt; color: #333; margin-top: 14px; }
  h4 { font-size: 11.5pt; color: #333; margin-top: 10px; }
  code { font-family: Courier, monospace; background-color: #f2f2f2; padding: 1px 3px; }
  pre { font-family: Courier, monospace; background-color: #f2f2f2; padding: 8px; font-size: 9.5pt;
        white-space: pre-wrap; border: 1px solid #ddd; }
  pre code { background-color: transparent; padding: 0; }
  a { color: #0366d6; text-decoration: none; }
  ul, ol { margin-top: 4px; margin-bottom: 4px; }
  li { margin-bottom: 3px; }
</style>
"""


def main():
    if len(sys.argv) != 3:
        print("Usage: python md_to_pdf.py <input.md> <output.pdf>")
        sys.exit(1)

    md_path, pdf_path = sys.argv[1], sys.argv[2]

    with open(md_path, encoding="utf-8") as f:
        md_text = f.read()

    body_html = markdown.markdown(
        md_text, extensions=["fenced_code", "tables", "toc"]
    )
    full_html = f"<html><head>{STYLE}</head><body>{body_html}</body></html>"

    with open(pdf_path, "wb") as out_file:
        result = pisa.CreatePDF(full_html, dest=out_file)

    if result.err:
        print(f"Error generating PDF: {result.err}")
        sys.exit(1)

    print(f"PDF written to {pdf_path}")


if __name__ == "__main__":
    main()
