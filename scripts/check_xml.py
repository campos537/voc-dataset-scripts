import cv2
from xml.etree import ElementTree
import os
import sys

def main(xml_directory,images_directory):
    for xml_file in os.listdir(xml_directory+"/"):
        image_name = xml_file[:-4] + ".jpg"
        tree = ElementTree.parse(xml_directory+"/"+xml_file)
        bnd_list = tree.findall("object/bndbox")
        name_list = tree.findall("object")
        img = cv2.imread(images_directory+"/"+image_name)
        print (images_directory+"/"+image_name)
        count = 0
        for item in bnd_list:
            print(name_list[count].findtext('name'))
            x = int(item.findtext('xmin'))
            y = int(item.findtext('ymin'))
            x_max = int(item.findtext('xmax'))
            y_max = int(item.findtext('ymax'))
            print("")
            cv2.rectangle(img,(x,y),(x_max,y_max),(255,0,255), 2)
            cv2.putText(img,name_list[count].findtext('name'),(x,y-10),1,2,(255,0,255))
            count += 1
        
        cv2.imshow("TEST",img)
        if cv2.waitKey(0) == 27:
            break
if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("usage: python check_xml.py xml_directory images_directory")
    else:
        main(sys.argv[1],sys.argv[2])