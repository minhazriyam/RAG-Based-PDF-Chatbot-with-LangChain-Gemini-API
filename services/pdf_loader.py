from PyPDF2 import PdfReader

def read_pdfs_to_text(files) -> str:
    text = []
    for f in files:
        reader = PdfReader(f)
        for p in reader.pages:
            t = p.extract_text() or ""
            text.append(t)
    return "\n".join(text)
