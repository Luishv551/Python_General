def extension(file):
    image = ["jpeg", "jpg" ,"png", "gif"]
    application = ["pdf", "zip"]
    octet_stream = ["bin"]
    text = ["txt"]

    file_extension = file.split(".")[-1].lower().strip()

    if file_extension == "jpg": file_extension = "jpeg"

    if file_extension in image:
        new_file = "image/" + file_extension
        return new_file

    elif file_extension in application:
        new_file = "application/" + file_extension
        return new_file

    elif file_extension in text:
        new_file = "text/" + "plain"
        return new_file

    elif file_extension in octet_stream or file_extension not in octet_stream:
        new_file = "application/" + "octet-stream"
        return new_file

    return "Unknown File Type!"

file_name = input("Type here the file name: ")
print(extension(file_name))
