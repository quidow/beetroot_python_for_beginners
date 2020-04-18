from lxml import etree
from bs4 import BeautifulSoup


def read_fop(file, step=1000000):
    with open(file) as f:
        f.seek(0, 2)  # Jumps to the end of file
        end_location = f.tell()  # Give you the end location (characters from start)
        f.seek(74)  # Jumps to the beginning of the file escaping useless part
        while not f.tell() == end_location:
            xml_str = '<DATA>' + f.read(step)
            while not xml_str[-10:] == '</SUBJECT>' and not f.tell() == end_location:
                xml_str += f.read(1)
            if not xml_str[-7:] == '</DATA>':
                xml_str += '</DATA>'
            yield xml_str


def find_fop(file, record=None, edrpou=None):
    for xml_str in read_fop(file):
        root = etree.fromstring(xml_str)
        for subject in root.getchildren():
            if record and subject.attrib['RECORD'] == str(record):
                return BeautifulSoup(etree.tostring(subject), "xml").prettify()
            for elem in subject.getchildren():
                if edrpou and elem.tag == 'EDRPOU' and elem.text == edrpou:
                    return BeautifulSoup(etree.tostring(subject), "xml").prettify()
