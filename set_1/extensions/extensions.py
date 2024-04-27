images = ["gif","jpg","jpeg","png"]
aplications = ["pdf","zip"]

def extension(str):
    splited = str.split(".")
    ext= splited[len(splited)-1]
    if (ext=="jpg"):
        ext="jpeg"
    if(len(splited)>1):
        if (ext in images):
            return "image/" + ext
        if (ext in aplications):
            return "application/" + ext
        if(ext == "txt"):
            return "text/plain"
    return "application/octet-stream"

print(extension(input("File name: ").strip().lower()))
