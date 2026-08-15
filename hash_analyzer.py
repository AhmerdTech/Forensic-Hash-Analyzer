import hashlib
import os

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


def main():
    print("=" * 50)
    print("       FORENSIC HASH ANALYZER")
    print("=" * 50)

    file_path = input("Enter the path to the evidence file: ")

    if not os.path.isfile(file_path):
        print("Error: File not found.")
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
