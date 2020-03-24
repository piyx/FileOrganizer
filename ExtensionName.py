def foldername(extension):
    if(extension == ""):
        return None
    else:
        switcher = {
            "exe" : "Software/Applications", 
            "txt" : "Notes/Text", 
            "pdf" : "PDFs", 
            "c"   : "Code", 
            "py"  : "Code",
            "java": "Code",
            "jpg" : "Images", 
            "png" : "Images",  
            "jpeg": "Images", 
            "raw" : "Images",
            "mp3" : "Music", 
            "mp4" : "Videos", 
            "mkv" : "Videos", 
        }
        return switcher.get(extension, "New Folder") #returns "New Folder" if not in dictionary