# _*_coding:utf8-

import optparse
from pyPdf import PdfFileReader
'''
This code we learning "How to extract information from PDF".
we need use ANONOPS_the_press_Release.pdf, you can use "wget" to download.
The "wget Url":
    wget http://www.wired.com/images_blogs/threatlevel/2010/12/ANONOPS_The_Press_Release.pdf
This code is very very easy.Right?
'''

def printMeta(fileName):
    '''
    :param fileName: target file name
    :return: None
    Docstring:
    ----------
        we using PdfFileReader() function to create session.
        the file() function like open() function.
        pdfFile.getDocumentInfo():
            extract information from PDF and return dictionary.
    '''
    pdfFile = PdfFileReader(file(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print '[*] PDF MetaData For: ' + str(fileName)
    for metaItem in docInfo:
        print '[+] ' + metaItem + ':' + docInfo[metaItem]


def main():
    parser = optparse.OptionParser('usage % prog ' + '-F <PDF file name>')
    parser.add_option('-F', dest='fileName', type='string', help='specify PDF file name or path')
    (options, args) = parser.parse_args()
    fileName = options.fileName
    if fileName is None:
        print parser.usage
        exit(0)
    else:
        printMeta(fileName)


if __name__ == '__main__':
    main()

'''
HomeWork:
        0. Familiar with code.
        1. Trying yourself PDF files with this code.
        Note, The PDF file should use PDF tool,not create '.pdf' file!!
'''
