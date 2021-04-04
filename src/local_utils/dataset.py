def clean_dataset():
    import os

    data_path = os.path.abspath(os.path.join(__file__, '..', '..', '..', 'data'))

    files = os.listdir(data_path)

    appropriate_files = []
    for file in filter(lambda x: x.endswith('.xml'), files):
        if f'{file[:-4]}.jpg' in files:
            appropriate_files.append(f'{file[:-4]}.jpg')
        else:
            os.remove(os.path.join(data_path, file))

    for file in filter(lambda x: x.endswith('.jpg'), files):
        if file not in appropriate_files:
            os.remove(os.path.join(data_path, file))

    max_letter_count_for_file = len(str(len(appropriate_files)))

    i = 0
    for file in appropriate_files:
        if file[:-4] != str(i).zfill(max_letter_count_for_file):
            os.rename(os.path.join(data_path, file),
                      os.path.join(data_path, f'{str(i).zfill(max_letter_count_for_file)}.jpg'))
            os.rename(os.path.join(data_path, f'{file[:-4]}.xml'),
                      os.path.join(data_path, f'{str(i).zfill(max_letter_count_for_file)}.xml'))

        i += 1


if __name__ == '__main__':
    clean_dataset()
