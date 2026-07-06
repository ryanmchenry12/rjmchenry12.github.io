from pathlib import Path

pdf_lines = [
    "%PDF-1.4",
    "1 0 obj",
    "<< /Type /Catalog /Pages 2 0 R >>",
    "endobj",
    "2 0 obj",
    "<< /Type /Pages /Kids [3 0 R] /Count 1 >>",
    "endobj",
    "3 0 obj",
    "<< /Type /Page /Parent 2 0 R /MediaBox [0 0 612 792] /Contents 4 0 R /Resources << /Font << /F1 5 0 R >> >> >>",
    "endobj",
    "4 0 obj",
    "<< /Length 81 >>",
    "stream",
    "BT /F1 18 Tf 72 720 Td (Ryan McHenry - Cybersecurity & IT Graduate) Tj ET",
    "endstream",
    "endobj",
    "5 0 obj",
    "<< /Type /Font /Subtype /Type1 /BaseFont /Helvetica >>",
    "endobj",
]

pdf = "\n".join(pdf_lines) + "\n"

# Build xref table with correct offsets
parts = []
offsets = [0]
current = "%PDF-1.4\n"
for line in pdf_lines:
    offsets.append(len(current.encode("latin-1")))
    current += line + "\n"

# Rebuild with correct offsets
pdf = "%PDF-1.4\n"
offsets = []
for line in pdf_lines:
    offsets.append(len(pdf.encode("latin-1")))
    pdf += line + "\n"

xref_offset = len(pdf.encode("latin-1"))
pdf += "xref\n0 6\n"
pdf += "0000000000 65535 f \n"
for off in offsets[1:]:
    pdf += f"{off:010d} 00000 n \n"
pdf += f"trailer\n<< /Size 6 /Root 1 0 R >>\nstartxref\n{xref_offset}\n%%EOF\n"

Path("resume.pdf").write_bytes(pdf.encode("latin-1"))
print("Created resume.pdf")
