from flask import Blueprint, render_template, request, redirect, url_for, flash, session
from app.models import Users, Instructors, Courses, Enrollments
from app import db
from datetime import date

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/')
def index():
    return redirect(url_for('auth.login'))



# --- SIGNUP / REGISTER ---
@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        email = request.form['email']
        password = request.form['password']

        # check if email already exists
        existing_user = Users.query.filter_by(email=email).first()
        if existing_user:
            flash("Email already registered. Please login.", "warning")
            return redirect(url_for('auth.login'))

        # create new user
        new_user = Users(username=username, email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Account created successfully! Please login.", "success")
        return redirect(url_for('auth.login'))

    return render_template('register.html')


# --- LOGIN ---
@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

             # --- Admin Login ---
        if email == "admin@gmail.com" and password == "admin":
            session['user_id'] = 0
            session['username'] = 'Admin'
            session['is_admin'] = True
            flash("Welcome, Admin!", "success")
            return redirect(url_for('auth.admin_dashboard'))
        
        # --- Normal User Login ---
        user = Users.query.filter_by(email=email, password=password).first()
        if user:
            session['user_id'] = user.user_id
            session['username'] = user.username
            session['is_admin'] = False
            flash("Login successful!", "success")
            return redirect(url_for('auth.home'))
        else:
            flash("Invalid email or password.", "danger")

    return render_template('login.html')


# --- USER HOME ---
@auth_bp.route('/home')
def home():
    if 'user_id' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('auth.login'))

    user = Users.query.get(session['user_id'])
    enrollments = Enrollments.query.filter_by(user_id=user.user_id).all()
    all_courses = Courses.query.all()

    return render_template('home.html', user=user, enrollments=enrollments, courses=all_courses)

# --- ENROLL INTO COURSE ---
@auth_bp.route('/enroll/<int:course_id>')
def enroll(course_id):
    if 'user_id' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('auth.login'))

    user_id = session['user_id']
    existing = Enrollments.query.filter_by(user_id=user_id, course_id=course_id).first()

    if existing:
        flash("Already enrolled in this course.", "info")
    else:
        new_enrollment = Enrollments(
            user_id=user_id,
            course_id=course_id,
            enrollment_date=date.today(),
            status='Active'
        )
        db.session.add(new_enrollment)
        db.session.commit()
        flash("Successfully enrolled!", "success")

    return redirect(url_for('auth.home'))

# --- ADMIN DASHBOARD ---
@auth_bp.route('/admin_dashboard')
def admin_dashboard():
    if 'is_admin' not in session or not session['is_admin']:
        flash("Unauthorized access.", "danger")
        return redirect(url_for('auth.login'))

    users = Users.query.all()
    instructors = Instructors.query.all()
    courses = Courses.query.all()
    enrollments = Enrollments.query.all()

    return render_template(
        'admin_dashboard.html',
        users=users,
        instructors=instructors,
        courses=courses,
        enrollments=enrollments
    )
# --- UPDATE USER INFO ---
@auth_bp.route('/update_user', methods=['GET', 'POST'])
def update_user():
    if 'user_id' not in session:
        flash("Please login first.", "warning")
        return redirect(url_for('auth.login'))

    user = Users.query.get(session['user_id'])

    if request.method == 'POST':
        new_username = request.form['username']
        new_email = request.form['email']
        new_password = request.form['password']

        # Update fields
        user.username = new_username
        user.email = new_email
        user.password = new_password

        db.session.commit()
        flash("Profile updated successfully!", "success")
        return redirect(url_for('auth.home'))

    return render_template('update_user.html', user=user)


# --- LOGOUT ---
@auth_bp.route('/logout')
def logout():
    session.clear()
    flash('''Logged out successfully.
           Login again to continue''', "info")
    return redirect(url_for('auth.login'))


