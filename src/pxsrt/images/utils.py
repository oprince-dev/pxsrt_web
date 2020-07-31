import os
import secrets
from PIL import Image
from pxsrt import app
from pxsrt.pxsrt import PxSrt


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
    path = os.path.join(app.root_path, 'static/img/' + folder, upload.filename)
    if folder == 'profpics':
        upload = crop_thumbnail(upload)
    upload.save(path)
    return upload.filename


def instantiate_pxsrt_obj(filename):
    file = os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename)
    pxsrt_obj = PxSrt(file)

    return pxsrt_obj
