# html2pdf.py
# convert html to pdf with pdfkit

import pdfkit
import sys
import os

# html = sys.argv[1]
# html_base = os.path.splitext(html)[0]
html_base = './test'
pdf_out = html_base + '.pdf'

options = {
      'page-size': 'A4',
      # 'margin-top': '0.1in',
      # 'margin-right': '0.1in',
      # 'margin-bottom': '0.1in',
      # 'margin-left': '0.1in',
      'encoding': "UTF-8",
      #'no-outline': None
      'javascript-delay': '10000'
}

# pdfkit.from_file(html, pdf_out, options=options)
pdfkit.from_url('https://plot.ly/~tallidea/7966.embed?showlink=false', pdf_out, options=options)