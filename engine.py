import easyocr
from rapidfuzz import process, fuzz
from parser import parse_prescription
from medicine_scan import scan_medicine_image
from decision_engine import check_and_log_dose

# Initialize OCR reader
reader = easyocr.Reader(['en'], gpu=False)

def extract_text(image_path):
    results = reader.readtext(image_path)
    text = " ".join([r[1] for r in results])
    return text

def match_medicine(scanned, medicine_list):
    if not medicine_list:
        return False, None, 0

    match, score, _ = process.extractOne(
        scanned,
        medicine_list,
        scorer=fuzz.partial_ratio
    )

    return score > 70, match, score


if __name__ == "__main__":
    print("=== MEDICINE AI ENGINE ===")

    image_path = "prescription.jpg"

    print("\nReading prescription image...")
    extracted_text = extract_text(image_path)
    print("\nExtracted Text:\n", extracted_text)

    prescription_data = parse_prescription(extracted_text)

    print("\nStructured Prescription:")
    for med, info in prescription_data.items():
        print(med, "->", info)

    while True:
        img = input("\nEnter medicine image filename (or exit): ")

        if img == "exit":
            print("Exiting...")
            break

        scanned_words = scan_medicine_image(img)

        if not scanned_words:
            print("❌ Could not read medicine name")
            continue

        scanned = scanned_words[0]
        print("Scanned medicine:", scanned)

        medicine_names = list(prescription_data.keys())
        found, match, score = match_medicine(scanned, medicine_names)

        if found:
            info = prescription_data[match]
            allowed_timings = info["timing"]

            ok, message = check_and_log_dose(match, allowed_timings)
            print(message)

            if ok:
                print(f"TAKE {match.upper()}")
                print("Dose:", info["dose"])
                print("Timing:", info["timing"])
        else:
            print("❌ NOT IN PRESCRIPTION")
