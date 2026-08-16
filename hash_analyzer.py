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
    print("=" * 60)
    print("             FORENSIC FILE ANALYZER")
    print("=" * 60)

    # Case information
    case_id = input("Enter Case ID: ")
    evidence_id = input("Enter Evidence ID: ")
    examiner = input("Enter Examiner Name: ")
    description = input("Enter Evidence Description: ")

    # Evidence file
    file_path = input("\nEnter the path to the evidence file: ")

    if not os.path.isfile(file_path):
        print("\nError: File not found.")
        return

    file_info = os.stat(file_path)

    created = datetime.fromtimestamp(file_info.st_ctime)
    modified = datetime.fromtimestamp(file_info.st_mtime)

    md5, sha1, sha256 = calculate_hashes(file_path)

    print("\n")
    print("=" * 60)
    print("              FORENSIC ANALYSIS REPORT")
    print("=" * 60)

    print("\nCASE INFORMATION")
    print("-" * 60)
    print("Case ID:", case_id)
    print("Evidence ID:", evidence_id)
    print("Examiner:", examiner)
    print("Description:", description)

    print("\nFILE INFORMATION")
    print("-" * 60)
    print("File Name:", os.path.basename(file_path))
    print("File Size:", file_info.st_size, "bytes")
    print("Created:", created)
    print("Modified:", modified)

    print("\nCRYPTOGRAPHIC HASHES")
    print("-" * 60)
    print("MD5:", md5)
    print("SHA-1:", sha1)
    print("SHA-256:", sha256)

    print("\n" + "=" * 60)
    print("Analysis completed successfully.")
    print("=" * 60)


if __name__ == "__main__":
    main()
