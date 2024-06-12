# Jeffa Triana Putra
# Membuat program yang dapat menghasilkan file csv yang berisikan report student dan report subject
import pandas as pd

def report_student(student_name): #Fungsi untuk memanggil data siswa yang sudah diolah
    # TODO 1 : Baca csv file dari tabel student sebagai s dan exam_result sebagai e terlebih dahulu
    s = pd.read_csv("student.csv")
    e = pd.read_csv("exam_result.csv")

    # TODO 2 : Gabungkan tabel exam_result dan student dengan menyamakan student_id yang ada pada kedua tabel
    x = pd.merge(s, e, on = "student_id")

    # TODO 3:
    # Cari rata-rata dari setiap siswa pada setiap ujiannya (exam 1 dan exam 2)
    # kelompokkan rata-rata berdasarkan student_id, student_name, dan exam_event
    grouped_student = x[['student_id', 'student_name', 'exam_score', 'exam_event']].groupby(['student_id','student_name','exam_event'])
    average_exam = (grouped_student.mean())
    # TODO 4 : Pisah antara exam_1 dan exam_2 dengan menggunakan fungsi head dan tail
    sorted_exam_1 = average_exam.sort_values(by=['exam_event'], ascending=True).head(24)
    sorted_exam_2 = average_exam.sort_values(by=['exam_event'], ascending=True).tail(24)

    # TODO 5 : Gabungkan kembali nilai ujian 1 dan ujian 2 yang sudah dirata-rata setiap siswanya dengan menyamakan nama siswa
    avg_stud = pd.merge(sorted_exam_1, sorted_exam_2, on = "student_name")
    # TODO 6 : Hitung rata-rata dari ujian 1 dan ujian 2
    avg_stud['average_exam_score'] = avg_stud[['exam_score_x', 'exam_score_y']].mean(axis=1)
    # TODO 7 : Buat grade berdasarkan rata-rata total ujian 1 dan ujian 2
    avg_stud.loc[(avg_stud['average_exam_score'] >= 90), 'Grade'] = 'A'
    avg_stud.loc[(avg_stud['average_exam_score'] >= 80) & (avg_stud['average_exam_score'] < 90), 'Grade'] = 'B'
    avg_stud.loc[(avg_stud['average_exam_score'] >= 70) & (avg_stud['average_exam_score'] < 80), 'Grade'] = 'C'
    avg_stud.loc[(avg_stud['average_exam_score'] >= 50) & (avg_stud['average_exam_score'] < 70), 'Grade'] = 'D'
    avg_stud.loc[(avg_stud['average_exam_score'] < 50), 'Grade'] = 'F'

    # TODO 8 : Simpan report final ke dalam CSV
    print(student_name)
    final_report_student = (avg_stud.loc[student_name])
    print(final_report_student)
    final_report_student.to_csv(f'/Users/dzno9/Desktop/TechnicalTestDE_Jeffa Triana Putra/output/report_{student_name}_from_python.csv', index=False)


def report_subject(subject_name):
    # Baca csv file dari tabel subject sebagai sb dan exam_result sebagai e terlebih dahulu
    e = pd.read_csv("exam_result.csv")
    sb = pd.read_csv("subject.csv")

    # Gabungkan tabel subject dan exam_result dengan menyamakan subject_id yang ada pada kedua tabel
    y = pd.merge(sb, e, on="subject_id")

    # Cari rata-rata dari setiap subject pada setiap ujiannya
    # kelompokkan rata-rata berdasarkan subject_id, subject_name, dan exam_event
    grouped_subject = y[['subject_id', 'subject_name', 'exam_score', 'exam_event']].groupby(['subject_id', 'subject_name', 'exam_event'])
    average_subject = (grouped_subject.mean())

    # Pisah antara exam_1 dan exam_2 dengan menggunakan fungsi head dan tail
    subject_exam_1 = average_subject.sort_values(by=['exam_event'], ascending=True).head(6)
    subject_exam_2 = average_subject.sort_values(by=['exam_event'], ascending=True).tail(6)

    avg_sub = pd.merge(subject_exam_1, subject_exam_2, on="subject_name")
    avg_sub['average_exam_score'] = avg_sub[['exam_score_x', 'exam_score_y']].mean(axis=1)

    avg_sub.loc[(avg_sub['average_exam_score'] >= 90), 'Grade'] = 'A'
    avg_sub.loc[(avg_sub['average_exam_score'] >= 80) & (avg_sub['average_exam_score'] < 90), 'Grade'] = 'B'
    avg_sub.loc[(avg_sub['average_exam_score']) >= 70 & (avg_sub['average_exam_score'] < 80), 'Grade'] = 'C'
    avg_sub.loc[(avg_sub['average_exam_score'] >= 50) & (avg_sub['average_exam_score'] < 70), 'Grade'] = 'D'
    avg_sub.loc[(avg_sub['average_exam_score']) < 50, 'Grade'] = 'F'
    print(subject_name)
    # Simpan report final ke dalam CSV
    final_report_subject=(avg_sub.loc[subject_name])
    print(final_report_subject)
    final_report_subject.to_csv(f'/Users/dzno9/Desktop/TechnicalTestDE_Jeffa Triana Putra/output/report_{subject_name}_from_python.csv', index=False)