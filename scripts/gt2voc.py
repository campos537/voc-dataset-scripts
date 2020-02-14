import os
import sys
# reload(sys)
# sys.setdefaultencoding('utf-8')
import xml.etree.ElementTree as ET
import cv2

def normal_bounding(list_input_output):
	name_equal = ""
	count_names = 0
	name_classes = []
	count_classes = []

	line_prev = ""
	total = 0
	output_directory = list_input_output[(len(list_input_output)-1)]
	if not os.path.isdir((output_directory+'/Annotations/')):
		os.mkdir((output_directory+'/Annotations/'))
	if not os.path.isdir((output_directory+'/JPEGImages/')):
		os.mkdir((output_directory+'/JPEGImages/'))
	with open((output_directory+"/dataset_gt.gt"),"r") as normal, open((output_directory+"/trainval.txt"),'w') as file1:
		name_dataset = output_directory.split("/")[(len(output_directory.split("/"))-1)]
		count = 0
		flag_test = False		

		for line in normal:
			found_image = False
			line_split = line.split(" ")
			for dataset in list_input_output:
				if dataset != output_directory:
					if os.path.exists((dataset+"/"+line_split[0]+".jpg")):
						found_image = True
						print (("FOUND =D "+line_split[0]+".jpg"))
						if name_equal != line_split[0]:
							img = cv2.imread((dataset+"/"+line_split[0]+".jpg"), 1)
							if not img is None:
								height_, width_, channels_ = img.shape
								annotation = ET.Element('annotation')
								

								folder = ET.SubElement(annotation, 'folder')
								filename = ET.SubElement(annotation, 'filename')
								source =  ET.SubElement(annotation, 'source')
								owner = ET.SubElement(annotation, 'owner')
								size = ET.SubElement(annotation, 'size')
								segmented = ET.SubElement(annotation, 'segmented')
								
								folder.text = name_dataset 
								filename.text = line_split[0]

								database = ET.SubElement(source , 'database')
								anno = ET.SubElement(source , 'annotation')
								image = ET.SubElement(source , 'image')

								database.text = name_dataset
								anno.text = name_dataset
								image.text = name_dataset

								flickrid = ET.SubElement(owner , 'flickrid')
								name = ET.SubElement(owner , 'name')
								

								flickrid.text = 'Openimage'
								name.text = 'Openimage'
								
								depth = ET.SubElement(size , 'depth')
								width = ET.SubElement(size , 'width')
								height = ET.SubElement(size, 'height')

								depth.text = '3'
								width.text = str(width_)
								height.text = str(height_)
								
								segmented.text = '0'						

								obj1 = ET.SubElement(annotation, 'object')
								name1 = ET.SubElement(obj1,'name')
								bndbox = ET.SubElement(obj1,'bndbox')
								name1.text = line_split[5].split('\n')[0]
								xmin = ET.SubElement(bndbox,'xmin')
								ymin = ET.SubElement(bndbox,'ymin')
								xmax = ET.SubElement(bndbox,'xmax')
								ymax = ET.SubElement(bndbox,'ymax')

								xmin.text = str(int(float(line_split[1])*float(width_)))
								ymin.text = str(int(float(line_split[2])*float(height_)))
								xmax.text = str(int(float(line_split[3])*float(width_)))
								ymax.text = str(int(float(line_split[4])*float(height_)))						
								
								if name_equal == line_split[0]:
									count_names = count_names+1
								elif name_equal != line_split[0]:
									count_names = 0
								
								flag_test = True	
								total = total + 1
								count = 0				

						if name_equal == line_split[0]:
							print(name_equal, " " , line_split[0])
							obj1 = ET.SubElement(annotation, 'object')
							name1 = ET.SubElement(obj1,'name')
							bndbox = ET.SubElement(obj1,'bndbox')
							name1.text = line_split[5].split('\n')[0]
							xmin = ET.SubElement(bndbox,'xmin')
							ymin = ET.SubElement(bndbox,'ymin')
							xmax = ET.SubElement(bndbox,'xmax')
							ymax = ET.SubElement(bndbox,'ymax')

							xmin.text = str(int(float(line_split[1])*float(width_)))
							ymin.text = str(int(float(line_split[2])*float(height_)))
							xmax.text = str(int(float(line_split[3])*float(width_)))
							ymax.text = str(int(float(line_split[4])*float(height_)))
							count = count + 1
							flag_test = False
						elif name_equal != line_split[0] and flag_test == True:
							count = count + 1
							flag_test = False
							name_equal = line_split[0]
						else:
							print ("current name :  " , line_split[0], " equal name : ", name_equal, "flag_test " , flag_test)	

						if(count >= 1 and name_equal == line_split[0]):
							tree = ET.ElementTree(annotation)
							tree.write((output_directory+'/Annotations/'+line_split[0]+'.xml'))
							if not os.path.isfile((output_directory+'/JPEGImages/'+line_split[0]+'.jpg')):
								cv2.imwrite((output_directory+'/JPEGImages/'+line_split[0]+'.jpg'),img)
							line = ('JPEGImages/'+(line_split[0]+'.jpg')+' '+'Annotations/'+(line_split[0]+'.xml\n'))
							if line_prev != line:
								if not line_split[5].split('\n')[0] in name_classes:
									name_classes.append(line_split[5].split('\n')[0])
									count_classes.append(1)
								else:
									count_classes[name_classes.index(line_split[5].split('\n')[0])] += 1
								file1.write(line)
							line_prev = line	
						name_equal = line_split[0]
						
					if found_image == False:	
						found_image = False
			if found_image == False:
				print (("NOT FOUND "+line_split[0]+".jpg"))

	for animal in name_classes:
		print ("class: " + animal + " quantity: " + str(count_classes[name_classes.index(animal)]))

def main(list_input_output):
	normal_bounding(list_input_output)
if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("usage: python gt2voc.py input_dataset input_dataset2... output_directory")
	else:
		count_arg = 1
		list_input_output = []
		while(count_arg != len(sys.argv)):
			list_input_output.append(sys.argv[count_arg])
			print (sys.argv[count_arg])
			count_arg = count_arg + 1
		main(list_input_output)
