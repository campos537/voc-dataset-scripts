# VOC Object Detection Scripts

## Description

The idea of this repository is to help people generate and test custom datasets for the VOC format in order to be able train Object Detection models.

## Usage of gt2voc script
to help in the creation of the dataset a script was made to convert a ground truth with the format below (named `dataset_gt.gt`)

`name_of_image x0 y0 x1 y1 class_name`

to the VOC format that has an xml to each image.

* The position is in percent of the image
* the name of the image is without te extension (.jpg,.png)

To run the script it needs to have installed `opencv-python` and `xml`.

after that just run:
```
cd scripts
python gt2voc.py path/to/image/folder/ path/to/image/folder2/ path/to/output/folder/
```
* the dataset_gt.gt file needs to be inside the output folder

## Additional scripts

The `check_xml.py` helps to check if the bounding boxes are in the right part of the image
```
cd scripts
python check_xml.py xml_directory images_directory
```

The `count_objects_xml.py` helps to count how many objects each class has for the specific text file with the annotations in order to help generating the test.txt file.
```
cd scripts
python count_objects_xml.py text_file
```
