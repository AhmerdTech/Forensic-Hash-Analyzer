import hashlib
import os
from datetime import datetime


def calculate_hashes(file_path):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while True:
            data = file.read(4096)

            if not data:
                break

            md5.update(data)
            sha1.update(data)
            sha256.update(data)

    return md5.hexdigest(), sha1.hexdigest(), sha256.hexdigest()


def main():
    print("=" * 50)
    print("        FORENSIC FILE ANALYZER")
    print("=" * 50)

    file_path = input("Enter the path to the evidence file: ")

    if not os.path.isfile(file_path):
        print("Error: File not found.")
        return

    file_info = os.stat(file_path)

    print("\nFILE INFORMATION")
    print("-" * 50)

    print("File name:", os.path.basename(file_path))
    print("File size:", file_info.st_size, "bytes")

    created = datetime.fromtimestamp(file_info.st_ctime)
    modified = datetime.fromtimestamp(file_info.st_mtime)

    print("Created:", created)
    print("Modified:", modified)

    print("\nCALCULATING HASHES...")
    
    md5, sha1, sha256 = calculate_hashes(file_path)

    print("\nCRYPTOGRAPHIC HASHES")
    print("-" * 50)

    print("MD5:", md5)
    print("SHA-1:", sha1)
    print("SHA-256:", sha256)

    print("\n" + "=" * 50)
    print("Analysis completed successfully.")
    print("=" * 50)


if __name__ == "__main__":
    main()
