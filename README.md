# VOC Object Detection Scripts

## Description

The idea of this repository is to help people generate and test custom datasets for the VOC format in order to be able train Object Detection models.

## Usage of gt2voc script
1. Create a file named `dataset_gt.gt` using the format below:
    `name_of_image x0 y0 x1 y1 class_name`
2. then just run the `gt2voc.py` script following the instructions below:

```
cd scripts
python gt2voc.py path/to/image/folder/ path/to/image/folder2/ path/to/output/folder/
```
* the dataset_gt.gt file needs to be inside the output folder.
* The position is in percent of the image (eg: `person1 0.2 0.1 0.4 0.5 person`)
* the name of the image is without te extension (.jpg,.png)

To run the script it needs to have installed `opencv-python` and `xml`.



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
