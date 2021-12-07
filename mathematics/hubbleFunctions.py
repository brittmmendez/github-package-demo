def get_file_name_without_path_and_extension(value):
    a = value.split("/")
    fileName = a[len(a)-1]
    try:
        pos = fileName.rindex(".")
        return fileName[0:pos]
    except Exception as e:
        print(e)
        return fileName