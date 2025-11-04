from app import db

class Users(db.Model):
    __tablename__ = 'Users'

    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=False)

    enrollments = db.relationship('Enrollments', back_populates='user')

    def __repr__(self):
        return f"<User {self.username}>"


class Instructors(db.Model):
    __tablename__ = 'Instructors'

    instructor_id = db.Column(db.Integer, primary_key=True)
    instructor_name = db.Column(db.String(50), nullable=False)
    expertise = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(15))

    courses = db.relationship('Courses', back_populates='instructor')

    def __repr__(self):
        return f"<Instructor {self.instructor_name}>"


class Courses(db.Model):
    __tablename__ = 'Courses'

    course_id = db.Column(db.Integer, primary_key=True)
    course_name = db.Column(db.String(100), nullable=False)
    instructor_id = db.Column(db.Integer, db.ForeignKey('Instructors.instructor_id'))
    duration = db.Column(db.String(20))

    instructor = db.relationship('Instructors', back_populates='courses')
    enrollments = db.relationship('Enrollments', back_populates='course')

    def __repr__(self):
        return f"<Course {self.course_name}>"


class Enrollments(db.Model):
    __tablename__ = 'Enrollments'

    enrollment_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('Users.user_id'))
    course_id = db.Column(db.Integer, db.ForeignKey('Courses.course_id'))
    enrollment_date = db.Column(db.Date)
    status = db.Column(db.String(20))

    user = db.relationship('Users', back_populates='enrollments')
    course = db.relationship('Courses', back_populates='enrollments')

    def __repr__(self):
        return f"<Enrollment {self.enrollment_id}>"
