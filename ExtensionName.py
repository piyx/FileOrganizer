def foldername(extension):
    if(extension == ""):
        return None
    else:
        switcher = {
            "exe"  : "Software", 
            "txt"  : "Notes-Text", 
            "pdf"  : "PDFs", 
            "c"    : "C programs", 
            "py"   : "Python files",
            "java" : "Java programs",
            "class": "Java programs", 
            "cpp"  : "Cpp programs", 
            "jpg"  : "Images", 
            "png"  : "Images",  
            "jpeg" : "Images", 
            "raw"  : "Images",
            "mp3"  : "Music", 
            "mp4"  : "Videos", 
            "mkv"  : "Videos",
        }
        return switcher.get(extension, "Extras") #returns "New Folder" if not in dictionary