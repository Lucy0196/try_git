print "____INPUT DATA____"
nim = raw_input("Masukan NIM Anda : ")
nama = raw_input("Masukan Nama : ")
alamat = raw_input("Masukan Alamat : ")
kelas = raw_input("Masukan Kelas Anda : ")
smester = raw_input("Masukan Smester Anda : ")

harian = input("Masukan Nilai Harian : ")
uts = input("Masukan Nilai UTS : ")
uas = input("Masukan Nilai UAS : ")

print "_______HASIL________"

print "NIM 	: ",nim
print "Nama 	: ",nama
print "Alamat 	: ",alamat
print "Kelas 	: ",kelas
print "Smester : ",smester

total = (harian + uts + uas)/3
print "Nilai rata - rata anda : ",total

grade = ""

if(total<=100 and total>=90):
	grade = "A"
elif(total<=89 and total>=70):
	grade = "B"
elif(total<=69 and total>=50):
	grade = "C"
elif(total<=49 and total>=30):
	grade = "D"
else:
	grade = "E"

print "Grade Anda : ",grade
print "_________________________"