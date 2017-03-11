import xml.etree.ElementTree as ET
from apiv2.search.utils import latex_symbols as ls

prefix = '@string/'

def parse_symbol_tree():
    string_arrays = {}
    symbols = {}
    strings = {}
    root = ET.fromstring(ls.XML_SYMBOLS_STR)
    for child in root:
        if child.tag == 'string-array':
            string_arrays[child.attrib['name'].upper()] = []
            for item in child:
                string_arrays[child.attrib['name'].upper()].append(item.text[len(prefix):].upper())
        if child.tag == 'string':
            element_name = child.attrib['name']
            if "formula" in element_name:
                symbols[element_name.upper()] = child.text
            else:
                strings[element_name.upper()] = child.text
    print("STRING_ARRAYS = ")
    print(string_arrays)
    print("STRINGS = ")
    print(strings)
    print("LATEX_SYMBOLS = ")
    print(symbols)
    return string_arrays, strings, symbols
    # print(strings)