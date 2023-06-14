import xmltodict
from PIL import Image

with open("types.labels") as file:
    data = file.read()
    list = data.split('\n')


def name_index(name):
    return list.index(name)


# 1713 entries
for i in range(1, 1714):
    with open(f"Annotations/{i}.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    im = Image.open(f"Images/{i}.jpg")
    # To normalize the values of required in yolo
    w, h = im.size
    with open(f"Annotations_in_txt/{i}.txt", 'a') as data_file:
        if not data_dict['annotation'] == None:
            try:
                for object in data_dict['annotation']['object']:
                    # print(object)
                    x_min = int(object['bndbox']['xmin'])
                    x_max = int(object['bndbox']['xmax'])
                    y_min = int(object['bndbox']['ymin'])
                    y_max = int(object['bndbox']['ymax'])
                    x_center = (x_min + x_max) / (2 * w)
                    y_center = (y_min + y_max) / (2 * h)
                    x_width = (x_max - x_min) / w
                    y_width = (y_max - y_min) / h
                    index = name_index(object['name'])
                    data = f"{index} {x_center} {y_center} {x_width} {y_width} \n"
                    data_file.write(data)
                    # print(x_center, y_center, x_width, y_width)
            except TypeError:
                # print(data_dict['annotation']['object'])
                x_min = int(data_dict['annotation']['object']['bndbox']['xmin'])
                x_max = int(data_dict['annotation']['object']['bndbox']['xmax'])
                y_min = int(data_dict['annotation']['object']['bndbox']['ymin'])
                y_max = int(data_dict['annotation']['object']['bndbox']['ymax'])
                x_center = (x_min + x_max) / (2 * w)
                y_center = (y_min + y_max) / (2 * h)
                x_width = (x_max - x_min) / w
                y_width = (y_max - y_min) / h
                index = name_index(data_dict['annotation']['object']['name'])
                data = f"{index} {x_center} {y_center} {x_width} {y_width}"
                data_file.write(data)
                # print(x_center, y_center, x_width, y_width)
