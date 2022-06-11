import urllib.request
import xml.dom.minidom as minidom

def get_data(xml_url):
    try:
        web_file = urllib.request.urlopen(xml_url)
        return web_file.read()
    except:
        pass



def get_currencies_dictionary(xml_content):

    dom = minidom.parseString(xml_content)
    dom.normalize()

    elements = dom.getElementsByTagName("Valute")
    currency_dict = {}

    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Nominal':
                    quant = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'Value':
                    if child.firstChild.nodeType == 3:
                        value = float(child.firstChild.data.replace(',', '.')) / quant
                if child.tagName == 'Name':
                    if child.firstChild.nodeType == 3:
                        char_code = child.firstChild.data
        currency_dict[char_code] = value
    return currency_dict


def get_ex_currency(curr_name, xml_content):
    dom = minidom.parseString(xml_content)
    dom.normalize()

    t = False

    elements = dom.getElementsByTagName("Valute")
    for node in elements:
        for child in node.childNodes:
            if child.nodeType == 1:
                if child.tagName == 'Nominal':
                    quant = float(child.firstChild.data.replace(',', '.'))
                if child.tagName == 'Name':
                    if child.firstChild.nodeType == 3:
                        if child.firstChild.data == curr_name:
                            t = True
                if child.tagName == 'Value' and t == True:
                    if child.firstChild.nodeType == 3:
                        return float(child.firstChild.data.replace(',', '.')) / quant

def print_dict(dict):
    for key in dict.keys():
        print(key, dict[key])
