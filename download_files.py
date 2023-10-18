import requests
import os
import zipfile

# Define the directory where you want to save the downloaded files and the extracted files
download_directory = "downloaded_files"
extracted_directory = "extracted_files"

# Create the directories if they don't exist
if not os.path.exists(download_directory):
    os.makedirs(download_directory)

if not os.path.exists(extracted_directory):
    os.makedirs(extracted_directory)

# Read links from the text file
with open("download_links.txt", "r") as file:
    urls = file.read().splitlines()

# Download and extract files
for url in urls:
    # Extract the filename from the URL
    file_name = os.path.join(download_directory, url.split("/")[-1])
    
    try:
        # Send an HTTP GET request to the URL without SSL certificate verification
        response = requests.get(url, verify=False)
    
        if response.status_code == 200:
            # If the request is successful, write the file to the specified directory
            with open(file_name, "wb") as file:
                file.write(response.content)
            print(f"Downloaded {file_name}")
            
            # Extract the downloaded file
            with zipfile.ZipFile(file_name, 'r') as zip_ref:
                zip_ref.extractall(extracted_directory)
                print(f"Extracted {file_name} to {extracted_directory}")
                
            # Delete the downloaded zip file if needed
            os.remove(file_name)
        else:
            print(f"Failed to download {url}")
    except requests.exceptions.RequestException as e:
        print(f"Failed to connect to {url}: {str(e)}")

print("All downloads and extractions completed.")
