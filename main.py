import psycopg2
from datetime import date

DB_CONFIG = {
    "dbname": "",
    "user": "",
    "password": "",
    "host": "",
    "port": "",
}


def get_connection():
    return psycopg2.connect(**DB_CONFIG)


def getAllStudents():
    conn = get_connection()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM students;")
        rows = cursor.fetchall()
        print("Current Students:")
        for row in rows:
            print(
                f"ID: {row[0]} | Name: {row[1]} {row[2]} | Email: {row[3]} | Enrolled: {row[4]}"
            )
    except Exception as e:
        print(f"Error fetching students: {e}")
    finally:
        cursor.close()
        conn.close()


def addStudent(first_name, last_name, email, enrollment_date):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s);"
        cursor.execute(query, (first_name, last_name, email, enrollment_date))
        conn.commit()
        print(
            f"Successfully added student: {first_name} {last_name}, {email}, {enrollment_date}"
        )
    except Exception as e:
        conn.rollback()
        print(f"Error adding student: {e}")
    finally:
        cursor.close()
        conn.close()


def updateStudentEmail(student_id, new_email):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "UPDATE students SET email = %s WHERE student_id = %s;"
        cursor.execute(query, (new_email, student_id))
        conn.commit()
        print(
            f"Successfully updated email for student with ID {student_id} to {new_email}"
        )
    except Exception as e:
        conn.rollback()
        print(f"Error updating student email: {e}")
    finally:
        cursor.close()
        conn.close()


def deletestudent(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    try:
        query = "DELETE FROM students WHERE student_id = %s;"
        cursor.execute(query, (student_id,))
        conn.commit()
        print(f"Successfully deleted student with ID {student_id}")
    except Exception as e:
        conn.rollback()
        print(f"Error deleting student: {e}")
    finally:
        cursor.close()
        conn.close()


def main():
    # getAllStudents()

    # addStudent("john", "smith", "john.smith@example.com", date(2024, 1, 3))
    # getAllStudents()

    # updateStudentEmail(1, "john.updated@example.com")
    # getAllStudents()

    deletestudent(3)
    getAllStudents()


main()
