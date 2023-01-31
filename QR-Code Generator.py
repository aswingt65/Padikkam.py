import qrcode

print("Enter the data : ")
img = qrcode.make(input())
img.save('qrcode.jpg')
print('QR code saved as qrcode.jpg')