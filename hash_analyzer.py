import hashlib
import os
from datetime import datetime


def calculate_hashes(file_path):
    hashes = {
        "MD5": hashlib.md5(),
        "SHA-1": hashlib.sha1(),
        "SHA-256": hashlib.sha256()
    }

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            for hash_object in hashes.values():
                hash_object.update(chunk)

    return {name: h.hexdigest() for name, h in hashes.items()}


def get_metadata(file_path):
    file_info = os.stat(file_path)

    return {
        "File Name": os.path.basename(file_path),
        "File Size": f"{file_info.st_size} bytes",
        "Created": datetime.fromtimestamp(
            file_info.st_ctime
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "Modified": datetime.fromtimestamp(
            file_info.st_mtime
        ).strftime("%Y-%m-%d %H:%M:%S"),
        "Accessed": datetime.fromtimestamp(
            file_info.st_atime
        ).strftime("%Y-%m-%d %H:%M:%S")
    }


def main():
    print("=" * 60)
    print("             FORENSIC FILE ANALYZER")
    print("=" * 60)

    file_path = input("Enter the path to the evidence file: ")

    if not os.path.isfile(file_path):
        print("\nError: File not found.")
        return

    print("\nAnalyzing evidence...\n")

    metadata = get_metadata(file_path)
    hashes = calculate_hashes(file_path)

    print("FILE METADATA")
    print("-" * 60)

    for name, value in metadata.items():
        print(f"{name}: {value}")

    print("\nCRYPTOGRAPHIC HASHES")
    print("-" * 60)

    for algorithm, value in hashes.items():
        print(f"{algorithm}: {value}")

    print("\n" + "=" * 60)
    print("Analysis completed successfully.")
    print("=" * 60)


if name == "main":
    main()
