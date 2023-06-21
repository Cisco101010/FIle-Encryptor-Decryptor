import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def generate_key(password):
    salt = b'\x93\xd0\xbf\xdbG7Bp\xb5(\xad\xe2oQ\xba'
    kdf = PBKDF2HMAC(
        algorithm=hashes.SHA256(),
        length=32,
        salt=salt,
        iterations=100000,
        backend=default_backend()
    )
    key = kdf.derive(password.encode())
    encoded_key = base64.urlsafe_b64encode(key)
    return encoded_key

def decrypt_file(file_path, key):
    try:
        if not os.path.isfile(file_path):
            raise ValueError(f"The file '{file_path}' does not exist or is not a valid file.")

        file_name, file_extension = os.path.splitext(file_path)

        if file_extension.lower() != '.enc':
            raise ValueError(f"The file '{file_path}' does not have a valid '.enc' extension for decryption.")

        with open(file_path, 'rb') as file:
            encrypted_content = file.read()

        fernet = Fernet(key)
        decrypted_content = fernet.decrypt(encrypted_content)

        decrypted_file_path = file_name[:-8] + file_extension

        with open(decrypted_file_path, 'wb') as file:
            file.write(decrypted_content)

        os.remove(file_path)

        print(f"File '{file_path}' decrypted successfully.'{decrypted_file_path}'.")

    except Exception as e:
        print(f"Error while decrypting the file '{file_path}': {str(e)}")

def decrypt_directory(directory_path, key):
    try:
        if not os.path.isdir(directory_path):
            raise ValueError(f"The directory '{directory_path}' does not exist or is not a valid directory.")

        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                decrypt_file(file_path, key)

    except Exception as e:
        print(f"Error while decrypting the directory '{directory_path}': {str(e)}")

def main():
    try:
        # Imprime el banner en color rojo
        print("\033[31m")
        print("****************************************")
        print("*         D4RK ARMY                    *")
        print("*                                      *")
        print("*       Decrypt files                  *")
        print("*                                      *")
        print("*    Powered by cisco_101              *")
        print("*                                      *")
        print("****************************************")
        print("\033[0m")

        # Obtiene la ruta del directorio a desencriptar
        directory_path = input("Ingrese la ruta del directorio a desencriptar: ").strip()

        # Obtiene la clave de desencriptación del usuario
        decryption_key = input("Ingrese la clave de desencriptación: ").strip()

        # Verifica si el directorio existe y es válido
        if not os.path.isdir(directory_path):
            print(f"El directorio '{directory_path}' no existe o no es un directorio válido.")
            return

        # Verifica si la clave de desencriptación es válida
        if not decryption_key:
            print("Clave de desencriptación inválida.")
            return

        # Genera la clave a partir de la clave de desencriptación
        key = generate_key(decryption_key)

        # Desencripta el directorio
        decrypt_directory(directory_path, key)

        # Guarda la clave generada en un archivo
        key_file_path = os.path.join(directory_path, "encryption_key.txt")
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)

        print(f"Clave generada guardada en el archivo: {key_file_path}")

    except Exception as e:
        print(f"Error al ejecutar el programa: {str(e)}")

if __name__ == "__main__":
    main()
