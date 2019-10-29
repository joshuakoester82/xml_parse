import xml.etree.ElementTree as ET
import pandas as pd
import sys


def xml_to_dict(root,xml_dict=None):
    if xml_dict is None:
        xml_dict = {}

    if xml_dict.get(root.tag) is None:
        xml_dict[root.tag] = dict_to_str(root.attrib) + str(root.text)
    else:
        xml_dict[root.tag] += "\n" + dict_to_str(root.attrib) + str(root.text)

    for child in root:
        xml_to_dict(child, xml_dict)
    return xml_dict


def write_to_excel(data, filename, sheetname="Sheet1"):
    # Create data frame
    data = pd.DataFrame(data)
    # Write to excel
    datatoexcel = pd.ExcelWriter(filename, engine='xlsxwriter')
    data.to_excel(datatoexcel, sheet_name=sheetname)
    datatoexcel.save()


def dict_to_str(dict):
    dict_list = []
    for key, value in dict.items():
        dict_list.append(f"{str(key)}: {str(value)}")
    return ", ".join(dict_list)

def main():
    # Get xml files to convert from command line arguments
    for i, arg in enumerate(sys.argv):
        if i > 0:
            try:
                tree = ET.parse(arg)
                root = tree.getroot()
                dict_list = []
                for child in root:
                    dict_list.append(xml_to_dict(child))
                export_name = arg.replace(".xml", ".xlsx")
                write_to_excel(dict_list, export_name)
            except:
                print(f"Something went wrong converting {arg} to excel.")


if __name__ == "__main__":
    main()








