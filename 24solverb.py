import time
import math

cmd = input("Masukan daftar angka: ").split(" ")
idxlist = 0
count = 0
n1 = (cmd[0])
n2 = (cmd[1])
n3 = (cmd[2])
n4 = (cmd[3])
start = time.time()
temp = [n1, n2, n3, n4] #penampung nilai angka input sementara untuk dikocok
ls = ['+', '-', '/', '*'] #penampung operator
listoflist = [] #penampung array susuanan angka
mini = 24 - (8/(3 - (8/3))) #credit: Aditya Putra S., untuk mengeliminasi yang angkanya 8 3 8 3 atau semacamnya yang memiliki nilai 23.999999 yang tidak dapat dideteksi python
print("Daftar Solusi: \n")
for w in range (0,4):
	for q in range (0,4):
		for r in range (0,4):
			for s in range (0,4):
				idx = [w, q, r, s] #index untuk dikocok agar angka bervariasi
				no = [temp[w], temp[q], temp[r], temp[s]] #penampung kocokan angka
				if (idx[0] == idx[1] or idx[0] == idx[2] or idx[0] == idx[3] or idx[1] == idx[2] or idx[1] == idx[3] or idx[2] == idx[3]):
					pass
				else:
					if (no in listoflist):
						pass
					else:
						for i in range (0,4):
								for j in range (0,4):
									for k in range (0,4):
										a = ['(', no[0], ls[i], no[1], ')', ls[j], '(', no[2], ls[k], no[3], ')'] #susunan kurung 1
										b = ''.join(a)
										try:
											if (eval(b) == 24 or ((eval(b) >= (24-mini)) and (eval(b) <= 24))):
												print(b, '=', int(eval(b)))
												count += 1
										except ZeroDivisionError:
											pass
						for i in range (0,4):
							for j in range (0,4):
								for k in range (0,4):
									a = ['(', '(', no[0], ls[i], no[1],')', ls[j], no[2],')', ls[k], no[3]] #susunan kurung 2
									b = ''.join(a)
									try:
										if (eval(b) == 24 or ((eval(b) >= (24-mini)) and (eval(b) <= 24))):
											print(b, '=', math.ceil(eval(b)))
											count += 1
									except ZeroDivisionError:
										pass
						for i in range (0,4):
							for j in range (0,4):
								for k in range (0,4):
									a = ['(', no[0], ls[i], '(',no[1], ls[j], no[2],')',')', ls[k], no[3]] #susunan kurung 3
									b = ''.join(a)
									try:
										if (eval(b) == 24 or ((eval(b) >= (24-mini)) and (eval(b) <= 24))):
											print(b, '=', math.ceil(eval(b)))
											count += 1
									except ZeroDivisionError:
										pass
						for i in range (0,4):
							for j in range (0,4):
								for k in range (0,4):
									a = [no[0], ls[i], '(', '(', no[1], ls[j], no[2], ')', ls[k], no[3],')'] #susunan kurung 4
									b = ''.join(a)
									try:
										if (eval(b) == 24 or ((eval(b) >= (24-mini)) and (eval(b) <= 24))):
											print(b, '=', math.ceil(eval(b)))
											count += 1
									except ZeroDivisionError:
										pass
										
						for i in range (0,4):
							for j in range (0,4):
								for k in range (0,4):
									a = [no[0], ls[i], '(',  no[1], ls[j],  no[2],  ls[k], no[3],')'] #susunan kurung 5
									b = ''.join(a)
									try:
										if (eval(b) == 24 or ((eval(b) >= (24-mini)) and (eval(b) <= 24))):
											print(b, '=', math.ceil(eval(b)))
											count += 1
									except ZeroDivisionError:
										pass
						listoflist.append(no)
end = time.time()
print("\nJumlah solusi: ", count)
print("\nWaktu eksekusi: ", end-start)