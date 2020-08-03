from flask import render_template, url_for, flash, redirect, request, abort, Blueprint
from flask_login import current_user, login_required
from pxsrt import db
from pxsrt.models import Upload
from pxsrt.images.utils import crop_thumbnail, save_image, instantiate_pxsrt_obj
from pxsrt.images.forms import UploadForm, ToolsForm
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
    tools_form = ToolsForm()
    image = Upload.query.get_or_404(upload_id)
    if tools_form.validate_on_submit():
        pxsrt_obj = instantiate_pxsrt_obj(image.filename)
        pxsrt_obj.load_image_data()
        pxsrt_obj.set_user_choices(
                                    tools_form.mode.data,
                                    tools_form.threshold.data,
                                    tools_form.direction.data,
                                    tools_form.upper.data,
                                    tools_form.reverse.data
        )
        pxsrt_obj.read_thresh()

        if 'preview' in request.form:
            t_filename = pxsrt_obj.generate_thresh()
            image.t_filename = t_filename
            db.session.commit()
            return redirect(url_for('images.view_thresh', upload_id=upload_id))

        elif 'sort' in request.form:
            s_filename = pxsrt_obj.sort_pixels()
            image.s_filename = s_filename
            db.session.commit()
            return redirect(url_for('images.view_sort', upload_id=upload_id))

        elif 'refresh' in request.form:
            # Future AJAX
            pass

    return render_template('image.html', image=image, tools_form=tools_form)

@images.route('/image/<int:upload_id>/preview', methods=['GET', 'POST'])
@login_required
def view_thresh(upload_id):
    image = Upload.query.get_or_404(upload_id)
    return render_template('viewThresh.html', image=image)

@images.route('/image/<int:upload_id>/sorted', methods=['GET', 'POST'])
@login_required
def view_sort(upload_id):
    image = Upload.query.get_or_404(upload_id)
    return render_template('viewSort.html', image=image)

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
