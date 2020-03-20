{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "    # pdf_merger.py\n",
    "    import glob\n",
    "    from PyPDF2 import PdfFileWriter, PdfFileReader\n",
    "    def merger(output_path, input_paths):\n",
    "        pdf_writer = PdfFileWriter()\n",
    "        for path in input_paths:\n",
    "            pdf_reader = PdfFileReader(path)\n",
    "            for page in range(pdf_reader.getNumPages()):\n",
    "                pdf_writer.addPage(pdf_reader.getPage(page))\n",
    "        with open(output_path, 'wb') as fh:\n",
    "            pdf_writer.write(fh)\n",
    "    if __name__ == '__main__':\n",
    "        paths = glob.glob('w9_*.pdf')\n",
    "        paths.sort()\n",
    "        merger('pdf_merger.pdf', paths)"
   ]
  }
 ],
 "metadata": {},
 "nbformat": 4,
 "nbformat_minor": 2
}
