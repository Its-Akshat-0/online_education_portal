from app import create_app, db
from app.models import Users, Instructors, Courses, Enrollments
from datetime import date

app = create_app()
app.app_context().push()

db.drop_all()
db.create_all()

# --- Admin user ---
admin = Users(username='admin', email='admin@example.com', password='admin')
db.session.add(admin)
# ---- Regular users ---
user1 = Users(username='rahul_k', email='rahul@gmail.com', password='rahul123')
user2 = Users(username='neha_s', email='neha@gmail.com', password='neha@456')
user3 = Users(username='arjun_t', email='arjun@gmail.com', password='arjun789')
user4 = Users(username='meera_p', email='meera@gmail.com', password='meera321')
user5 = Users(username='rohit_b', email='rohit@gmail.com', password='rohit111')
user6 = Users(username='aisha_r', email='aisha@gmail.com', password='aisha2025')
user7 = Users(username='vijay_m', email='vijay@gmail.com', password='vijay777')
user8 = Users(username='divya_k', email='divya@gmail.com', password='divya999')
user9 = Users(username='sahil_n', email='sahil@gmail.com', password='sahil222')
user10 = Users(username='tina_d', email='tina@gmail.com', password='tina333')
user11 = Users(username='alice', email='alice@example.com', password='alice123')
user12 = Users(username='bob', email='bob@example.com', password='bob123')


db.session.add_all([user1, user2, user3, user4, user5, user6, user7, user8, user9, user10, user11, user12])

# --- Instructors and Courses ---
inst1 = Instructors(instructor_name='Dr. Ramesh Kumar', expertise='Machine Learning', contact='9876543210')
inst2 = Instructors(instructor_name='Prof. Anjali Mehta', expertise='Web Development', contact='9998877665')
inst3 = Instructors(instructor_name='Dr. Sunil Rao', expertise='Data Science', contact='8887766554')
inst4 = Instructors(instructor_name='Prof. Kavita Sharma', expertise='Cybersecurity', contact='7776655443')
inst5 = Instructors(instructor_name='Dr. Amit Verma', expertise='Database Systems', contact='6665544332')
inst6 = Instructors(instructor_name='Prof. Reena Gupta', expertise='AI & Robotics', contact='9090909090')
inst7 = Instructors(instructor_name='Dr. Piyush Patel', expertise='Cloud Computing', contact='8989898989')
inst8 = Instructors(instructor_name='Prof. Neeraj Singh', expertise='Computer Networks', contact='9797979797')
inst9 = Instructors(instructor_name='Dr. Sneha Desai', expertise='Digital Marketing', contact='9898989898')
inst10 = Instructors(instructor_name='Prof. Manish Joshi', expertise='Software Testing', contact='9999999999')
inst11 = Instructors(instructor_name='John Doe', expertise='Python', contact='1234567890')
inst12 = Instructors(instructor_name='Jane Smith', expertise='Data Science', contact='9876543210')
db.session.add_all([inst1, inst2, inst3, inst4, inst5, inst6, inst7, inst8, inst9, inst10, inst11, inst12])
db.session.commit()
c1 = Courses(course_name='Intro to Machine Learning', instructor_id=inst1.instructor_id, duration='8 weeks')
c2 = Courses(course_name='Full Stack Web Dev', instructor_id=inst2.instructor_id, duration='10 weeks')
c3 = Courses(course_name='Data Science with Python', instructor_id=inst3.instructor_id, duration='12 weeks')
c4 = Courses(course_name='Ethical Hacking', instructor_id=inst4.instructor_id, duration='6 weeks')
c5 = Courses(course_name='SQL & Database Design', instructor_id=inst5.instructor_id, duration='4 weeks')
c6 = Courses(course_name='AI Fundamentals', instructor_id=inst6.instructor_id, duration='9 weeks')
c7 = Courses(course_name='AWS Cloud Essentials', instructor_id=inst7.instructor_id, duration='5 weeks')
c8 = Courses(course_name='Networking Basics', instructor_id=inst8.instructor_id, duration='6 weeks')
c9 = Courses(course_name='Digital Marketing Pro', instructor_id=inst9.instructor_id, duration='7 weeks')
c10 = Courses(course_name='Manual & Automation Testing', instructor_id=inst10.instructor_id, duration='5 weeks')
c11 = Courses(course_name='Python for Beginners', instructor_id=inst11.instructor_id, duration='4 weeks')
c12 = Courses(course_name='Advanced Data Science', instructor_id=inst12.instructor_id, duration='8 weeks')
db.session.add_all([c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12])
db.session.commit()

# --- Enrollments ---
e1 = Enrollments(user_id=user1.user_id, course_id=c1.course_id, status='In Progress', enrollment_date=date(2024, 11, 1))
e2 = Enrollments(user_id=user1.user_id, course_id=c2.course_id, status='Completed', enrollment_date=date(2024, 8, 15))
e3 = Enrollments(user_id=user2.user_id, course_id=c3.course_id, status='In Progress', enrollment_date=date(2024, 10, 20))
e4 = Enrollments(user_id=user3.user_id, course_id=c4.course_id, status='Dropped', enrollment_date=date(2024, 5, 1))
e5 = Enrollments(user_id=user4.user_id, course_id=c5.course_id, status='Completed', enrollment_date=date(2023, 12, 1))
e6 = Enrollments(user_id=user5.user_id, course_id=c6.course_id, status='In Progress', enrollment_date=date(2024, 9, 1))
e7 = Enrollments(user_id=user6.user_id, course_id=c7.course_id, status='Completed', enrollment_date=date(2024, 7, 20))
e8 = Enrollments(user_id=user7.user_id, course_id=c8.course_id, status='In Progress', enrollment_date=date(2024, 11, 5))
e9 = Enrollments(user_id=user8.user_id, course_id=c9.course_id, status='Completed', enrollment_date=date(2024, 6, 10))
e10 = Enrollments(user_id=user9.user_id, course_id=c10.course_id, status='In Progress', enrollment_date=date(2024, 10, 1))
e11 = Enrollments(user_id=user10.user_id, course_id=c11.course_id, status='Pending', enrollment_date=date(2024, 11, 15)) # Future date
e12 = Enrollments(user_id=user11.user_id, course_id=c12.course_id, status='Completed', enrollment_date=date(2024, 4, 1))

db.session.add_all([e1, e2, e3, e4, e5, e6, e7, e8, e9, e10, e11, e12])
db.session.commit()


print("✅ Database seeded successfully!")
