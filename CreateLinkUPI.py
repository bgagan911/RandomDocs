#   Generate UPI URL based on Specification Document 1.5
import sys, os, pyperclip
import urllib.parse
import qrcode, qrcode.image.svg
from qrcode.image.pure import PymagingImage


def generateURL(pa="xxxx@okaxis",
                pn="Payee Name",
                mc="0000",
                tid="06-December-2019",
                tr="BILL-0091",
                tn="Lunch at GLENS",
                am="10",
                mam='null',
                cu="INR",
                url="https://www.google.com"):
    """
    Documentation : Generate URL based on the parameters passed 
    Usage GenerateURL <PARAMS>
        <VPA Address>
        <PayeeName>
        <MCC>
        <Transaction ID>
        <Transaction Ref. #>
        <Transaction Note>
        <Transaction Amount>
        <Min. Transaction Amount>
        <Currency Code>
        <URL>
    """ 

    # Define Payload for URL Parser
    payload = urllib.parse.urlencode({"pa":pa, "pn":pn, "mc": mc, "tid":tid, "tr": tr, "tn": tn, "am": am, "mam": mam, "cu": cu, "url": url},quote_via=urllib.parse.quote)

    # Generate UPI Link
    link = "upi://pay?%s" % payload
    
    print("\nEncoded URL: \n",link)
    
    # Copy Link
    pyperclip.copy(link)
    
    return link

def GenerateQR(upilink):

    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
        )

    qr.add_data(upilink)
    qr.make(fit=True)
    
    # Generate QR Image on Terminal in ASCII Format
    qr.print_ascii()
    # Set Colors
    img = qr.make_image(fill_color="black", back_color="white")
    # Show Image    
    img.show()
    # Save Image
    img.save("QR.png")
    #Newimg = qrcode.make(upilink, image_factory=PymagingImage)


qr = generateURL(am="1000")
GenerateQR(qr)