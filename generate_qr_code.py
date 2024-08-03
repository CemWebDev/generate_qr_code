import qrcode
from PIL import Image, ImageDraw

large_url = 'https://github.com/SimplyProgYT'

qr = qrcode.QRCode(
    version=10, 
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)
qr.add_data(large_url)
qr.make(fit=True)

matrix = qr.get_matrix()
size = len(matrix)

img = Image.new('RGB', (size * 10, size * 10), (255, 255, 255))
draw = ImageDraw.Draw(img)
fill_color = (0, 102, 204)

for y in range(size):
    for x in range(size):
        if matrix[y][x]:
            draw.rectangle([x * 10, y * 10, x * 10 + 10, y * 10 + 10], fill=fill_color)

border_size = 2
draw.rectangle([0, 0, img.width, img.height], outline=(0, 0, 0), width=border_size)

img.save('qr_code.png')

