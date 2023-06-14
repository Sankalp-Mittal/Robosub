import xmltodict
# Number of elements 1713
names = []
for i in range(1, 1714):
    with open(f"Annotations/{i}.xml") as xml_file:
        data_dict = xmltodict.parse(xml_file.read())
    # print(data_dict)
    if not data_dict['annotation'] == None:
        try:
            for object in data_dict['annotation']['object']:
                if object['name'] not in names:
                    names.append(object['name'])
        except TypeError:
            if data_dict['annotation']['object']['name'] not in names:
                names.append(data_dict['annotation']['object']['name'])
    # print(i)

print(names)

with open("types.labels", 'a') as file:
    for name in names:
        file.write(f"{name}\n")