from flask import render_template, url_for, redirect, request, flash, Blueprint
from flask_login import login_user, logout_user, current_user, login_required
from pxsrt import db, bcrypt
from pxsrt.models import User
from pxsrt.users.forms import RegisterForm, LoginForm, UpdateAccountForm
from pxsrt.images.utils import save_image


users = Blueprint('users', __name__)


@users.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user and bcrypt.check_password_hash(user.password,
                                               form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            if next_page:
                return redirect(next_page)
            else:
                redirect(url_for('main.home'))

        else:
            flash('Login Failed', 'danger')
    return render_template('login.html', title='Login', form=form)


@users.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('main.home'))
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(
                                                        form.password.data
                                                        ).decode('utf-8')
        user = User(username=form.username.data,
                    email=form.email.data,
                    password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created. Welcome, {form.username.data}!', 'success')
        return redirect(url_for('users.login'))
    return render_template('register.html', title='Register', form=form)


@users.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('users.login'))


@users.route('/account', methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        if form.profpic.data:
            profpic_filename = save_image(form.profpic.data, 'profpics')
            current_user.profpic = profpic_filename
        current_user.username = form.username.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account successfully updated', 'success')
        return redirect(url_for('users.account'))
    elif request.method == 'GET':
        form.username.data = current_user.username
        form.email.data = current_user.email

    profpic = url_for('static',
                      filename='img/profpics/' + current_user.profpic)
    return render_template('account.html',
                           title='Account', form=form, profpic=profpic)
