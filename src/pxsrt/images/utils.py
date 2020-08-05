import os
import secrets
from PIL import Image
from pxsrt import app
from pxsrt.pxsrt import PxSrt


def crop_thumbnail(upload):
    fname = upload.filename
    img = Image.open(upload)
    cropped = img.crop(((img.width - min(img.size)) // 2,
                    (img.height - min(img.size)) // 2,
                    (img.width + min(img.size)) // 2,
                    (img.height + min(img.size)) // 2))
    thumbnail_size = (100, 100)
    cropped.thumbnail(thumbnail_size)
    return cropped, fname


def save_image(upload, folder):
    path = os.path.join(app.root_path, 'static/img/' + folder)
    if not os.path.exists(path):
        os.makedirs(path)
    filepath = os.path.join(path, upload.filename)
    if folder == 'profpics':
        cropped, fname = crop_thumbnail(upload)
        cropped.save(filepath)
        return fname
    else:
        upload.save(filepath)
        return upload.filename

def instantiate_pxsrt_obj(filename):
    file = os.path.join(app.config['UPLOADED_IMAGES_DEST'], filename)
    pxsrt_obj = PxSrt(file)

    return pxsrt_obj
