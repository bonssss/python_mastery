import qrcode as qr

url = "https://coder-profile-bons.vercel.app/"

qr_code = qr.make(url)
qr_code.save("coder_profile_qr.png")
print("QR code generated and saved as 'coder_profile_qr.png'")