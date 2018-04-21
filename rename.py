import os
def rename_files():
    file_list=os.listdir(r"C:\Users\sayal\Desktop\Python\prank")
    print(file_list)
    os.chdir(r"C:\Users\sayal\Desktop\Python\prank")
    
    for file_name in file_list:
        os.rename(file_name,file_name.strip("0123456789"))


rename_files()
