import easyocr
import sys
import time
import os

def list_files_in_folder(folder_path):
    try:
        # Get a list of all files and subdirectories in the specified folder
        items = os.listdir(folder_path)
        
        # Filter out subdirectories and list only files
        files = [item for item in items if os.path.isfile(os.path.join(folder_path, item))]
        
        return files
    except Exception as e:
        print("Error:", e)
        return []

# Replace 'folder_path' with the path of the folder you want to list files from
folder_path = "./testdata"

reader = easyocr.Reader(['de','en']) # this needs to run only once to load the model into memory


if (len(sys.argv) > 1):
        file = sys.argv[1]
        if not file_exists(os.path.exists(file)):
                print(f"The file '{file_path}' exists.")
                exit(1)        
        result = reader.readtext(file)
        print (result)

else:
        print (f"Running OCR for all files in folder {folder_path}")
        files_list = list_files_in_folder(folder_path)        
        start_time = time.time()
        for fname in files_list:                
                result = reader.readtext(os.path.join(folder_path, fname))
                print (result)
        runtime = time.time() - start_time
        print("\nRuntime per image:", runtime/len(files_list), "seconds")
