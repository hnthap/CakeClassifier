# Cake Classifier

## Usage
Create new file named "my_secrets.py". The file's content is:
```
data_zip_filepath = ... # Replace ... with the file path of the ZIP file
```
The folder after extracting the ZIP file is in the following structure:
```
Cake/
  |-- <1st label>/
    |-- 01.png
    |-- ...
  |-- <2nd label>/
    |-- ...
  |-- ...
```
Then, run the code in "hog.ipynb".
