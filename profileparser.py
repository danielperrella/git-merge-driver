import logging
import xml.etree.ElementTree as ET
import objectdefinition
import importlib

def printobjlist(mylist):
    for obj in mylist:
        print(obj)


def str_to_class(module_name, class_name):
    """Return a class instance from a string reference"""
    try:
        module_ = importlib.import_module(module_name)
        try:
            class_ = getattr(module_, class_name)()
        except AttributeError:
            logging.error('Class does not exist: ' + str(class_name))
    except ImportError:
        logging.error('Module does not exist')
    return class_ or None


def parse(pathname):
    mylist = []
    tree = ET.parse(pathname)
    root = tree.getroot()

    for elem in root:
        testelement = str_to_class('objectdefinition',elem.tag.split("}",1)[1] ) #Dynamic instantiation
        if objectdefinition.oneLineTag(testelement): #Single Tag
            testelement[elem.tag.split("}",1)[1] ] = elem.text
        for subelem in elem:
            testelement[subelem.tag.split("}",1)[1] ] = subelem.text
        mylist.append(testelement)
    print('Parser for ',pathname,' End')
    return mylist