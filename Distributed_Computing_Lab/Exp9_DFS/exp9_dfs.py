import os

# Note: The lab manual used Google Colab paths. 
# I have commented them out and used a local directory so it runs smoothly on your PC.

# from google.colab import drive
# drive.mount('/content/drive')
# DFS_STORAGE = "/content/drive/My Drive/DistributedFileSystem"

# Local Directory Fallback
DFS_STORAGE = "./DistributedFileSystem"

if not os.path.exists(DFS_STORAGE):
    os.makedirs(DFS_STORAGE)

print(f"Distributed File System initialized at: {DFS_STORAGE}")

def upload_file(filename, content):
    file_path = os.path.join(DFS_STORAGE, filename)
    with open(file_path, 'w') as file:
        file.write(content)
    print(f" File '{filename}' uploaded successfully!")

def list_files():
    files = os.listdir(DFS_STORAGE)
    print(" Files in DFS:", files)

def download_file(filename):
    file_path = os.path.join(DFS_STORAGE, filename)
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            content = file.read()
        print(f" Content of '{filename}':\n {content}")
    else:
        print(f" Error: File '{filename}' not found!")

if __name__ == "__main__":
    # Example Usage
    upload_file("testfile.txt", "This is a distributed file system test.")
    list_files()
    download_file("testfile.txt")