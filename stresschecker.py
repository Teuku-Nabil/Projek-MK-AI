print ("Selamat Datang, ke Aplikasi Stress Checker Kami!")
print ("Disini kami akan mengecek tingkat stress anda!")
print ("")

nama = input("Masukkan nama anda: ")
umur = int(input("Masukkan umur anda: "))
print("")


print("Silahkan Pilih Nilai yang Sesuai dengan Keadaan Anda!")
print("0. Tidak Sama Sekali")
print("1. Tidak Sering")
print("2. Cukup Sering")
print("3. Hampir Setiap Hari")
print("")

# Pertanyaan
print("Dalam Seminggu terakhir, Seberapa Sering Anda Mengalami Hal Berikut Ini?: ")
q1 = int(input("1. Saya merasa lelah dan tidak punya energi: "))
if q1 == 0:
    q1 = 0
elif q1 == 1:
    q1 = 1
elif q1 == 2:
    q1 = 2
elif q1 == 3:
    q1 = 3
else:
    print("Input Salah")
    exit()

q2 = int(input("2. Saya merasa cemas dan gelisah: "))
if q2 == 0:
    q2 = 0
elif q2 == 1:
    q2 = 1
elif q2 == 2:
    q2 = 2
elif q2 == 3:
    q2 = 3
else:
    print("Input Salah")
    exit()

q3 = int(input("3. Saya merasa tidak bisa berkonsentrasi: "))
if q3 == 0:
    q3 = 0
elif q3 == 1:
    q3 = 1
elif q3 == 2:
    q3 = 2
elif q3 == 3:
    q3 = 3
else:
    print("Input Salah")
    exit()

q4 = int(input("4. Saya merasa tidak punya semangat: "))
if q4 == 0:
    q4 = 0
elif q4 == 1:
    q4 = 1
elif q4 == 2:
    q4 = 2
elif q4 == 3:
    q4 = 3
else:
    print("Input Salah")
    exit()

q5 = int(input("5. Saya merasa tidak punya motivasi: "))
if q5 == 0:
    q5 = 0
elif q5 == 1:
    q5 = 1
elif q5 == 2:
    q5 = 2
elif q5 == 3:
    q5 = 3
else:
    print("Input Salah")
    exit()

q6 = int(input("6. Saya merasa tidak punya kepercayaan diri: "))
if q6 == 0:
    q6 = 0
elif q6 == 1:
    q6 = 1
elif q6 == 2:
    q6 = 2
elif q6 == 3:
    q6 = 3
else:
    print("Input Salah")
    exit()

q7 = int(input("7. Saya merasa makan dengan berlebihan: "))
if q7 == 0:
    q7 = 0
elif q7 == 1:
    q7 = 1
elif q7 == 2:
    q7 = 2
elif q7 == 3:
    q7 = 3
else:
    print("Input Salah")
    exit()

q8 = int(input("8. Saya merasa tidak punya keinginan untuk berinteraksi dengan orang lain: "))
if q8 == 0:
    q8 = 0
elif q8 == 1:
    q8 = 1
elif q8 == 2:
    q8 = 2
elif q8 == 3:
    q8 = 3
else:
    print("Input Salah")
    exit()

q9 = int(input("9. Saya merasa tidak punya keinginan untuk melakukan sesuatu: "))
if q9 == 0:
    q9 = 0
elif q9 == 1:
    q9 = 1
elif q9 == 2:
    q9 = 2
elif q9 == 3:
    q9 = 3
else:
    print("Input Salah")
    exit()
print("")

# Hasil
hasil = q1 + q2 + q3 + q4 + q5 + q6 + q7 + q8 + q9
print("Hasil Stress Checker: ", hasil)
if hasil < 10:
    print("Tingkat Stress Anda: Normal")
elif hasil < 20:
    print("Tingkat Stress Anda: Sedang")
elif hasil < 30:
    print("Tingkat Stress Anda: Tinggi")
else:
    print("Tingkat Stress Anda: Sangat Tinggi")
print("")