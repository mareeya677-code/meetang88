import sys
from PIL import Image

# เปิดไฟล์ .ico
ico_file = 'site-logo.ico'
img = Image.open(ico_file).convert('RGBA')

# สร้างภาพพื้นหลังโปร่งใส
# ขนาด 192x192
img_192 = img.resize((192, 192), Image.Resampling.LANCZOS)
img_192.save('icon-192.png', 'PNG')

# ขนาด 512x512
img_512 = img.resize((512, 512), Image.Resampling.LANCZOS)
img_512.save('icon-512.png', 'PNG')

print("สร้างไอคอน PNG สำเร็จ!")
