import shutil

GB = 1024**3
(total, used, free) = shutil.disk_usage("/")

def Total_Space():
    print("Total : %.2fGB" %(float(total)/GB))

def Used_Space():
    print("Used: %.2fGB" %(float(used)/GB))

def Free_Space():
    print("Free: %.2fGB" %(float(free)/GB))
