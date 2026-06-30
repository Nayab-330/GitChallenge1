import platform
if platform.system() == "Windows":
    print("Linux Distribution:", platform.freedesktop_os_release()["PRETTY_NAME"])
else:
    print("Not running Linux")
