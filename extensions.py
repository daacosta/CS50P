filename = input("File name: ").strip().lower()

periodindex = filename.rfind(".")

if periodindex < 0:
    extension = ""
    print("application/octet-stream")

else:
    extension = filename[periodindex:]
    match extension:
        case ".pdf":
            print("application/pdf")
        case ".aac":
            print("audio/aac")
        case ".abw":
            print("application/x-abiword")
        case ".apng":
            print("image/apng")
        case ".arc":
            print("application/x-freearc")
        case ".avif":
            print("image/avif")
        case ".avi":
            print("video/x-msvideo")
        case ".azw":
            print("application/vnd.amazon.ebook")
        case ".bin":
            print("application/octet-stream")
        case ".bmp":
            print("image/bmp")
        case ".bz":
            print("application/x-bzip")
        case ".bz2":
            print("application/x-bzip2")
        case ".cda":
            print("application/x-cdf")
        case ".csh":
            print("application/x-csh")
        case ".css":
            print("text/css")
        case ".csv":
            print("text/csv")
        case ".doc":
            print("application/msword")
        case ".docx":
            print("application/vnd.openxmlformats-officedocument.wordprocessingml.document")
        case ".eot":
            print("application/vnd.ms-fontobject")
        case ".epub":
            print("application/epub+zip")
        case ".gz":
            print("application/gzip")
        case ".gif":
            print("image/gif")
        case ".htm":
            print("text/html")
        case "html":
            print("text/html")
        case ".ico":
            print("image/vnd.microsoft.icon")
        case ".ics":
            print("text/calendar")
        case ".jar":
            print("application/java-archive")
        case ".jpeg":
            print("image/jpeg")
        case ".jpg":
            print("image/jpeg")
        case ".js":
            print("text/javascript")
        case ".json":
            print("application/json")
        case ".jsonld":
            print("application/ld+json")