# create zipfile

# import zipfile
# with zipfile.ZipFile("myzip.zip","w")as archive:
#     archive.write("C:/Users/Python/Documents/Manoop.txt")
#     archive.write("C:/Users/Python/Documents/midhun.txt")
# print("files created")



# import zipfile

# with zipfile.ZipFile('myzip.zip', 'w') as zipf:
#     zipf.write('manoop.txt', 'midhun.txt')

# import zipfile
# with zipfile.ZipFile('myzip.zip', 'r') as zipf:
#     with zipf.open('midhun.txt') as zip:
#         contents = zip.read().decode('utf-8')
# print(contents)



# import zipfile

# Open the ZIP file for reading
# with zipfile.ZipFile('myzip.zip', 'r') as zip_file:
#     # List the contents of the ZIP file
#     file_list = zip_file.namelist()
#     print("Contents of the ZIP file:", file_list)

#     # Extract all files from the ZIP archive
#     for file_name in file_list:
#         zip_file.extract(file_name, "C:/Users/Python/Downloads")





# new zip file


# import zipfile
# with zipfile.ZipFile("__pycache__/zippppp.zip.","w")as archive:
#     archive.write("C:/Users/Python/Documents/__pycache__/vivanya.txt")
#     archive.write("C:/Users/Python/Documents/__pycache__/red.txt")
# print("files created")



# import zipfile

# with zipfile.ZipFile('zippppp.zip', 'w') as zipf:
#     zipf.write('__pycache__/vivanya.txt', 'red.txt')

# import zipfile
# with zipfile.ZipFile('zippppp.zip', 'r') as zipf:
#     with zipf.open('red.txt') as zip:
#         contents = zip.read().decode('utf-8')
# print(contents)









