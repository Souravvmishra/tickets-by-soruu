import segno

def generate_qr_code(text_content, filename="qrcode.png"):
    """
    Generate QR code from the given text content and save it to a file.

    Parameters:
    text_content (str): The content to be encoded in the QR code.
    filename (str): The name of the file to save the QR code. Default is 'qrcode.png'.
    """
    qrcode = segno.make_qr(text_content)
    qrcode.save(filename)
