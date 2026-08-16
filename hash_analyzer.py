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


def create_report(case_id, evidence_id, examiner, description,
                  file_path, file_info, created, modified,
                  md5, sha1, sha256):

    report_name = f"{case_id}_{evidence_id}_forensic_report.txt"

    analysis_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    report = f"""
============================================================
                 FORENSIC ANALYSIS REPORT
============================================================

CASE INFORMATION
------------------------------------------------------------
Case ID: {case_id}
Evidence ID: {evidence_id}
Examiner: {examiner}
Evidence Description: {description}

FILE INFORMATION
------------------------------------------------------------
File Name: {os.path.basename(file_path)}
File Size: {file_info.st_size} bytes
Created: {created}
Modified: {modified}
Analysis Time: {analysis_time}

CRYPTOGRAPHIC HASHES
------------------------------------------------------------
MD5: {md5}
SHA-1: {sha1}
SHA-256: {sha256}

============================================================
                 END OF FORENSIC REPORT
============================================================
"""

    with open(report_name, "w") as report_file:
        report_file.write(report)

    return report_name


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

    report_name = create_report(
        case_id,
        evidence_id,
        examiner,
        description,
        file_path,
        file_info,
        created,
        modified,
        md5,
        sha1,
        sha256
    )

    print("\n" + "=" * 60)
    print("Analysis completed successfully.")
    print("=" * 60)

    print("\nReport created:")
    print(report_name)

    print("\nMD5:", md5)
    print("SHA-1:", sha1)
    print("SHA-256:", sha256)


if __name__ == "__main__":
    main()