import hashlib
import os

def calculate_hashes(file_path):
    md5 = hashlib.md5()
    sha1 = hashlib.sha1()
    sha256 = hashlib.sha256()

    with open(file_path, "rb") as file:
        while chunk := file.read(4096):
            for hash_object in hashes.values():
                hash_object.update(chunk)

    return {name: h.hexdigest() for name, h in hashes.items()}


def main():
    print("=" * 60)
    print("             FORENSIC FILE ANALYZER")
    print("=" * 60)

    case_id = input("Enter Case ID: ")
    evidence_id = input("Enter Evidence ID: ")
    examiner = input("Enter Examiner Name: ")
    description = input("Enter Evidence Description: ")

    file_path = input("\nEnter the path to the evidence file: ")

    if not os.path.isfile(file_path):
        print("\nError: File not found.")
        return

    print("\nCalculating hashes...\n")

    results = calculate_hashes(file_path)

    print(f"File: {os.path.basename(file_path)}")
    print("-" * 50)

    for algorithm, value in results.items():
        print(f"{algorithm}: {value}")

    print("-" * 50)
    print("Hash calculation completed.")


if __name__ == "__main__":
    main()