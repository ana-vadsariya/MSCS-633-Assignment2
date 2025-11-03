# Import the necessary module
import qrcode

# Function to generate QR code
def generate_qr(url, filename="qrcode.png"):
    """
    Generates a QR code for the given URL and saves it as an image file.
    
    Parameters:
    url (str): The URL or data to encode in the QR code
    filename (str): The filename to save the QR code image
    """
    # Create a QR code object
    qr = qrcode.QRCode(
        version=1,  # controls the size of the QR code (1 = smallest)
        error_correction=qrcode.constants.ERROR_CORRECT_H,  # high error correction
        box_size=10,  # size of each box in pixels
        border=4  # thickness of the border
    )
    
    # Add data to the QR code
    qr.add_data(url)
    qr.make(fit=True)
    
    # Create an image of the QR code
    img = qr.make_image(fill_color="black", back_color="white")
    
    # Save the image to a file
    img.save(filename)
    print(f"QR code generated and saved as {filename}")

# Example usage
if __name__ == "__main__":
    url_input = input("Enter the URL to generate QR code: ")
    generate_qr(url_input)
