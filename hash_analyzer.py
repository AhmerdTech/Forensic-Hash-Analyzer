import hashlib
import os
from datetime import datetime

from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors


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


def create_pdf_report(
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
):
    report_name = f"{case_id}_{evidence_id}_forensic_report.pdf"

    document = SimpleDocTemplate(
        report_name,
        pagesize=A4,
        rightMargin=20 * mm,
        leftMargin=20 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm
    )

    styles = getSampleStyleSheet()

    title = styles["Title"]
    heading = styles["Heading2"]
    normal = styles["BodyText"]

    story = []

    story.append(Paragraph("FORENSIC ANALYSIS REPORT", title))
    story.append(Spacer(1, 10))

    story.append(Paragraph("Case Information", heading))

    case_data = [
        ["Case ID", case_id],
        ["Evidence ID", evidence_id],
        ["Examiner", examiner],
        ["Description", description]
    ]

    case_table = Table(case_data, colWidths=[40 * mm, 120 * mm])
    case_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ]))

    story.append(case_table)
    story.append(Spacer(1, 15))

    story.append(Paragraph("File Information", heading))

    file_data = [
        ["File Name", os.path.basename(file_path)],
        ["File Size", f"{file_info.st_size} bytes"],
        ["Created", str(created)],
        ["Modified", str(modified)],
        ["Analysis Time", datetime.now().strftime("%Y-%m-%d %H:%M:%S")]
    ]

    file_table = Table(file_data, colWidths=[40 * mm, 120 * mm])
    file_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (0, -1), colors.lightgrey),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("FONTNAME", (0, 0), (0, -1), "Helvetica-Bold"),
    ]))

    story.append(file_table)
    story.append(Spacer(1, 15))

    story.append(Paragraph("Cryptographic Hashes", heading))

    hash_data = [
        ["Algorithm", "Hash Value"],
        ["MD5", md5],
        ["SHA-1", sha1],
        ["SHA-256", sha256]
    ]

    hash_table = Table(hash_data, colWidths=[40 * mm, 120 * mm])
    hash_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.black),
        ("BACKGROUND", (0, 0), (-1, 0), colors.lightgrey),
        ("FONTNAME", (0, 0), (-1, 0), "Helvetica-Bold"),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))

    story.append(hash_table)
    story.append(Spacer(1, 20))

    story.append(
        Paragraph(
            "This report was generated automatically by the Forensic File Analyzer.",
            normal
        )
    )

    document.build(story)

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

    print("\nAnalyzing evidence...")

    file_info = os.stat(file_path)

    created = datetime.fromtimestamp(file_info.st_ctime)
    modified = datetime.fromtimestamp(file_info.st_mtime)

    md5, sha1, sha256 = calculate_hashes(file_path)

    report_name = create_pdf_report(
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

    print("\nPDF report created:")
    print(report_name)


if __name__ == "__main__":
    main()
