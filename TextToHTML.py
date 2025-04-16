def TextToHTML(text):
    # Split by newline + tab (used to indicate new paragraphs)
    paragraphs = text.strip().split("\n    ")
    HTMLOutput = "\n".join(f'<p class="articleText">{p.strip()}</p>' for p in paragraphs if p.strip())
    return HTMLOutput

text=""" """
print(TextToHTML(text))
