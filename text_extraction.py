import re
from pdfminer.high_level import extract_pages, extract_text

# for page_layout in extract_pages('@somalibooks gabadhii-labada-reer-heshiisay.pdf'):
#     for elemment in page_layout:
#         print(elemment)

text = extract_text("@somalibooks gabadhii-labada-reer-heshiisay.pdf")

print(text)
