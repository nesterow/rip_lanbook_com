import sys, os, time, PyPDF2, glob, re


if __name__ == '__main__':

  pages = int(sys.argv[1])
  for i in range(1, pages):
      os.system('bash rip_page.sh ' + str(i))
      time.sleep(1)
      print('Page ' + str(i) + ' of ' + str(pages) + ' complete.')
  print('All pages ripped.')

  print('Converting to pdf...')
  os.system('svg2pdf -o "%(base)s.pdf" ./page*.svg')

  print('Merging pdfs...')
  pdfs = sorted(glob.glob("*.pdf"), key=lambda x: int(re.sub("[A-Za-z\-\.]", "", x)))
  mergeFile = PyPDF2.PdfFileMerger()
  for pdf in pdfs:
      mergeFile.append(PyPDF2.PdfFileReader(pdf, 'rb'))

  mergeFile.write("the_book.pdf")
  print('Done.')
