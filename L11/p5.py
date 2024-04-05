#P5 ==> wapp to copy a file

import os
src_filename = input("enter source filename ")
if os.path.exists(src_filename):
    dest_filename = input("enter dest filename ")
    try:
        with open(src_filename, "r") as sf:
            with open(dest_filename, "w") as df:
                data = sf.read()
                df.write(data)
                print("copy completed")
    except Exception as e:
        print("issue ",e)
else:
    print(src_filename, "does not exists ")