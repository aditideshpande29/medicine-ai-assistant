import easyocr

reader = easyocr.Reader(['en'], gpu=False)

def scan_medicine_image(image_path):
    """
    Extract probable medicine name from strip image
    """
    results = reader.readtext(image_path)

    words = []
    for r in results:
        text = r[1]
        if text.isalpha() and len(text) > 3:
            words.append(text.lower())

    return words
	