import os
import shutil
from xml.dom import minidom


def copy_file_config_XML(config_XML):
    """
    Copies files, scripted from the config_XML.xml
    :param config_XML:  The name of the file that contains
                        the options for copying the file
    :return: list with errors if there were conflicts when
             copying files, or returns a sheet with a record
             of successful copying
    """
    log = []
    try:
        xmldoc = minidom.parse(config_XML)
    except Exception as inst:
        log.append('{}'.format(inst))
        return log

    itemlist = xmldoc.getElementsByTagName('file')
    for tag_file in itemlist:
        source_path = os.path.join(
            tag_file.attributes['source_path'].value,
            tag_file.attributes['file_name'].value
            )
        destination_path = os.path.join(
            tag_file.attributes['destination_path'].value,
            tag_file.attributes['file_name'].value
            )
        if not os.path.exists(tag_file.attributes['destination_path'].value):
            os.makedirs(tag_file.attributes['destination_path'].value)
        try:
            shutil.copy2(source_path, destination_path)
        except Exception as inst:
            log.append("{}".format(inst))
        if not log:
            log.append("Copy completed successfully ")
    return log
