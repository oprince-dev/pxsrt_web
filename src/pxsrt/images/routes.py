from flask import render_template, url_for, flash, redirect, request, abort, Blueprint, jsonify, make_response
from flask_login import current_user, login_required
from pxsrt import db
from pxsrt.models import Upload
from pxsrt.images.utils import crop_thumbnail, save_image, instantiate_pxsrt_obj
from pxsrt.images.forms import UploadForm
from multiprocessing import Pool


images = Blueprint('images', __name__)

@images.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        if form.file.data:
            upload_filename = save_image(form.file.data, 'uploads')
            upload = Upload(filename=upload_filename, author=current_user)
            db.session.add(upload)
            db.session.commit()
            flash('File uploaded', 'success')
            return redirect(url_for('main.home'))
    return render_template('upload.html', title='File', form=form)


@images.route('/image/<int:upload_id>', methods=['GET', 'POST'])
@login_required
def image(upload_id):
    image = Upload.query.get_or_404(upload_id)

    return render_template('image.html', image=image)

@images.route('/image/preview', methods=['POST'])
@login_required
def view_thresh():
    upload_id = request.form['image_id']
    image = Upload.query.get_or_404(upload_id)
    pxsrt_obj = instantiate_pxsrt_obj(image.filename)
    pxsrt_obj.load_image_data()
    pxsrt_obj.set_user_choices(
                                request.form['mode'],
                                request.form['threshold'],
                                request.form['direction'],
                                None,
                                None
    )
    pxsrt_obj.read_thresh()
    t_filename = pxsrt_obj.generate_thresh()
    image.t_filename = t_filename
    db.session.commit()

    return jsonify({'result' : 'success', 'path' : 'img/thresh/', 'filename' : t_filename})

@images.route('/image/sort', methods=['POST'])
@login_required
def view_sort():
    upload_id = request.form['image_id']
    image = Upload.query.get_or_404(upload_id)
    pxsrt_obj = instantiate_pxsrt_obj(image.filename)
    pxsrt_obj.load_image_data()
    pxsrt_obj.set_user_choices(
                                request.form['mode'],
                                request.form['threshold'],
                                request.form['direction'],
                                None,
                                None
    )
    pxsrt_obj.read_thresh()
    s_filename = pxsrt_obj.sort_pixels()
    image.s_filename = s_filename
    db.session.commit()

    return jsonify({'result' : 'success', 'path' : 'img/sorts/', 'filename' : s_filename})

@images.route('/image/refresh', methods=['POST'])
@login_required
def refresh():
    upload_id = request.form['image_id']
    image = Upload.query.get_or_404(upload_id)

    return jsonify({'result' : 'success', 'path' : 'img/uploads/', 'filename' : image.filename})

@images.route('/image/<int:image_id>/delete', methods=['POST'])
@login_required
def delete_image(image_id):
    image = Upload.query.get_or_404(image_id)
    if image.author != current_user:
        abort(403)
    db.session.delete(image)
    db.session.commit()
    flash('Image Deleted', 'success')
    return redirect(url_for('main.home'))
