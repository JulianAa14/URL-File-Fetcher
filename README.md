# Download and Extract Files from URLs

This Python script allows you to download files from a list of URLs provided in a text file, and then extract them into a specified directory. The code uses the `requests` library for downloading and `zipfile` for extracting compressed files. It also handles errors gracefully and provides feedback during the process.

## Usage

1. **Set the Download and Extract Directories**

   You can specify the directories where you want to save the downloaded files and the extracted files by modifying the following lines in the code:

   ```python
   download_directory = "downloaded_files"
   extracted_directory = "extracted_files"
   ```

   If the directories do not exist, the script will create them for you.

2. **Create a List of Download Links**

   Create a text file named "download_links.txt" and add one URL per line. The script will read these links and download the corresponding files. Make sure the text file is in the same directory as the script.

3. **Running the Script**

   Execute the script by running it using a Python interpreter. It will read the links from "download_links.txt," download each file, and extract it to the specified directory. If the download is successful, the downloaded file will be deleted after extraction. If the script encounters an error while downloading or extracting, it will print an error message and continue to the next link.

   To run the script, use the following command in your terminal:

   ```bash
   python script_name.py
   ```

   Replace `script_name.py` with the name of the script file.

4. **Review the Output**

   The script will print messages to the console, indicating whether the download and extraction were successful or if there was an error. Once all downloads and extractions are completed, the script will print "All downloads and extractions completed."

## Dependencies

This script relies on the following Python libraries:

- `requests`: For making HTTP GET requests to download files.
- `zipfile`: For extracting ZIP files.
- `os`: For directory manipulation.
  
Please ensure you have these libraries installed before running the script. You can install missing dependencies using pip:

```bash
pip install requests
```

## Note

- The script uses the `verify=False` parameter when making HTTP GET requests, which disables SSL certificate verification. Use caution when downloading files from untrusted sources.

- This script is intended for educational purposes and can be extended or modified for specific use cases. Make sure you have the necessary permissions to download and extract files from the provided URLs.

- Always exercise caution when handling downloaded files, especially when deleting them automatically. Ensure the files are safe and contain no important data before deleting them.

- Make sure you have a stable internet connection while running the script to avoid interruptions during downloads.

- This script does not support authentication for download links that require login credentials. You would need to modify the script to handle such cases.

Enjoy downloading and extracting your files with ease!
