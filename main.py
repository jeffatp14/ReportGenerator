#Jeffa Triana Putra

from report_generator import *
import argparse

#Digunakan subparsers karena dapat memilih antara report_student atau report_subject
parser = argparse.ArgumentParser(description='Report Generator')
subparsers = parser.add_subparsers(dest='task_name', help='Task to perform')

# Parsing task student_report dan argument nama siswa
student_parser = subparsers.add_parser('report_student', help='Report for student')
student_parser.add_argument('student', type=str, help='Student name')

# Parsing task subject_report dan argument nama subject
subject_parser = subparsers.add_parser('report_subject', help='Report for subject')
subject_parser.add_argument('subject', type=str, help='Subject name')

al