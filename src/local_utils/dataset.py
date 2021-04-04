def clean_dataset():
    def remove_elem(parent, elem):
        el = parent.find(elem)
        if el:
            parent.remove(el)

    import os

    from src.local_utils.constants import IMAGES_PATH, ANNOTATIONS_PATH

    images = os.listdir(IMAGES_PATH)
    annotations = os.listdir(ANNOTATIONS_PATH)

    valid_images = []

    for annotation in annotations:
        img4annotation = f'{annotation[:-4]}.jpg'

        if img4annotation in images:
            valid_images.append(img4annotation)

            import xml.etree.ElementTree as ET

            tree = ET.parse(os.path.join(ANNOTATIONS_PATH, annotation))
            root = tree.getroot()

            remove_elem(root, 'folder')
            remove_elem(root, 'path')
            remove_elem(root, 'source')
            remove_elem(root, 'segmented')

            for elem in root.findall('object'):
                remove_elem(elem, 'pose')
                remove_elem(elem, 'truncated')
                remove_elem(elem, 'difficult')

            with open(os.path.join(ANNOTATIONS_PATH, annotation), mode='wb') as file:
                file.writelines(ET.tostringlist(root))
        else:
            os.remove(os.path.join(ANNOTATIONS_PATH, annotation))

    for image in images:
        if image not in valid_images:
            os.remove(os.path.join(IMAGES_PATH, image))

    max_filename_len = len(str(len(valid_images)))

    for i in range(len(valid_images)):
        filename = valid_images[i][:-4]
        if filename != str(i).zfill(max_filename_len):
            os.rename(os.path.join(IMAGES_PATH, valid_images[i]),
                      os.path.join(IMAGES_PATH, f'{str(i).zfill(max_filename_len)}.jpg'))
            os.rename(os.path.join(ANNOTATIONS_PATH, f'{filename}.xml'),
                      os.path.join(ANNOTATIONS_PATH, f'{str(i).zfill(max_filename_len)}.xml'))


def xml2csv():
    import os
    from glob import glob
    import pandas as pd
    import xml.etree.ElementTree as ET

    from src.local_utils.constants import ANNOTATIONS_PATH

    xmls = []

    for xml in glob(os.path.join(ANNOTATIONS_PATH, '*.xml')):
        tree = ET.parse(xml)
        root = tree.getroot()

        filename = root.find('filename')
        size = root.find('size')

        for elem in root.findall('object'):
            bndbox = elem.find('bndbox')
            try:
                value = (filename.text,
                         size[0].text,
                         size[1].text,
                         elem.find('name').text,
                         bndbox[0].text,
                         bndbox[1].text,
                         bndbox[2].text,
                         bndbox[3].text
                         )
                xmls.append(value)
            except TypeError as e:
                print(xml)
                print(e)

    df = pd.DataFrame(xmls, columns=['filename', 'width', 'height', 'class', 'xmin', 'ymin', 'xmax', 'ymax'])
    df.to_csv(os.path.join(ANNOTATIONS_PATH, 'labels.csv'))


if __name__ == '__main__':
    clean_dataset()
    xml2csv()

