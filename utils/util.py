def read_file(file_name):
    with open(file_name) as f:
        content = f.read().splitlines()
    return content
