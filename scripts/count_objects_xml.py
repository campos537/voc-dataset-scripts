from xml.etree import ElementTree
import os
import sys

def main(text_file):
    with open(text_file,'r') as trainval_test_file:
        count_objects = []
        classes_ = []
        count = 0
        path_to_xml = text_file.split('/')
        string_to_xml = ''
        for folder in path_to_xml:
            if not '.txt' in folder:
                string_to_xml = string_to_xml + '/' + folder

        for line in trainval_test_file: 
            xml_path = line.split(' ')[1]
            #print ((string_to_xml+'/'+xml_path.split("\n")[0]))
            tree = ElementTree.parse((string_to_xml+'/'+xml_path.split("\n")[0]))
            name_list = tree.findall("object")
            
            
            for name in name_list:
                if not name.findtext('name') in classes_:
                    classes_.append(name.findtext('name'))
                    count_objects.append(1)
                else:
                    index = classes_.index(name.findtext('name'))
                    count_objects[index] += 1
        for class_ in classes_:
            print('class : '+ class_ + " quantity : " + str(count_objects[count]))
            count += 1

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("usage: python count_objects_xml.py text_file")
    else:
        main(sys.argv[1])
