# File Encryption and Decryption

Writting in python 
- ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)


This Python program allows you to encrypt and decrypt files in a specified directory using the cryptography library.

## Features

- Encrypts files with valid extensions (e.g., .txt, .docx, .xlsx, .pdf).
- Generates a secure encryption key from a user-provided password using PBKDF2 with SHA-256.
- Encrypts files using Fernet symmetric encryption.
- Saves the generated encryption key in a separate file for future decryption.
- Decrypts encrypted files back to their original form.

## Requirements

- Python 3.6 or higher
- cryptography library

Install the required dependencies by running the following command:

```shell
$ pip install -r requirements.txt
```

#Run encryptor
```
$ python encrypt.py
```
Provide the path to the directory you want to encrypt when prompted.

Enter the encryption password when prompted.

The program will encrypt all files with valid extensions within the specified directory and its subdirectories. The original files will be deleted, and the encrypted files will be saved with a .enc extension.

The encryption key will be saved in a file named "encryption_key.txt" within the specified directory.

To decrypt the encrypted files:

Run the program by executing the following command in your terminal:

Run decryptor
```
$ python decrypt.py
```
Provide the path to the directory containing the encrypted files when prompted.

Enter the decryption password when prompted.

The program will decrypt all files with the .enc extension within the specified directory and its subdirectories. The encrypted files will be deleted, and the decrypted files will be saved with their original names and extensions.

The encryption key is required for decryption and should be saved in a file named "encryption_key.txt" within the specified directory.

Note: Make sure to keep the encryption key file secure and only share it with authorized individuals who need to decrypt the files.

Author
This program is powered by cisco_101 and is part of the D4RK ARMY project.

Please note that file encryption and decryption should be used responsibly and in compliance with applicable laws and regulations.


install ("linux") install git sudo apt-get install git 
```
$ git clone https://github.com/Cisco101010/FIle-Encryptor-Decryptor
$ cd FIle-Encryptor-Decryptor
$ pip install -r requirements.txt
$ chmod +x encrypt.py 
$ chmod +x decrypt.py
$ python3 encrypt.py
$ python3 decrypt.py
```

install ("Windows")   install gitbash https://git-scm.com/downloads
```
$ git clone https://github.com/Cisco101010/FIle-Encryptor-Decryptor
$ cd FIle-Encryptor-Decryptor
$ pip install -r requirements.txt
$ python encrypt.py
$ python decrypt.py
```




