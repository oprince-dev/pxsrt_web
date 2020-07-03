import os
import secrets
from PIL import Image
from pxsrt import app


def crop_thumbnail(upload):
    img = Image.open(upload)
    img = img.crop(((img.width - min(img.size)) // 2,
                    (img.height - min(img.size)) // 2,
                    (img.width + min(img.size)) // 2,
                    (img.height + min(img.size)) // 2))
    thumbnail_size = (100, 100)
    img.thumbnail(thumbnail_size)
    return img


def save_image(upload, folder):
    random_hex = secrets.token_hex(8)
    _, ext = os.path.splitext(upload.filename)
    filename = random_hex + ext
    path = os.path.join(app.root_path, 'static/img/' + folder, filename)
    if folder == 'profpics':
        upload = crop_thumbnail(upload)
    upload.save(path)
    return filename
