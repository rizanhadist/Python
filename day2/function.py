#function adalah fungsi/kumpulan perintah untuk komputer yang dibungkus dengan keyword def dan diakhiri 
# dengan ":" serta diikuti dengan indentasi/spasi yang bisa memiliki balikan(return) maupun tidak 

# def myFunctionHello():
#     print("Hello")

# def sayMyName(name):
#     print("You Right,", name)


# myFunctionHello()
# sayMyName("Heisenberg")



# #Function Return 
# def myFunctionHelloreturn():
#     return"Hello Return"

# #Trigger
# response = myFunctionHelloreturn()
# print(response)

#exxx
# def  add (num1 + num2):
#     return num1 + num2

# result = add(3, 4) #Output : 7
# print(result)
# print(add(1, 5)) #Output : 6


#Quiz
# def substrack(parameter1, parameter2):
#     print()
#     print("Pengurangan Parameter1 = " + str(parameter1) + " Dikurang Parameter2= " + str(parameter2) + " adalah",  parameter1 - parameter2)
#     print()

#Function Perkalian

# def multiply(argument1, argument2):
# print(argument1 * argument2)

# substrack(100, 20)
# multiply(3, 4)

def alat_pendeteksi_kategori_golongan_usia(input):
    if input > 0 and input < 18:
        return "Dia adalah Anak-Anak"
    elif input >= 18 and input < 60:
        return "Dia adalah orang dewasa"
    elif input >= 60 and input < 100:
        return "Dia sudah lansia"
    else:
        return "Meninggal"

# Example usage:

print(alat_pendeteksi_kategori_golongan_usia(20))


# contoh lain

def alat_pendeteksi_kategori_golongan_usia(input):
    #Jika usia subjek 0 - 17 tahun, maka subjek adalah 'Anak Kecil'
    if input > 0 and input < 18:
        print ("\nSubject Anak Kecil!\n") 
    #Jika usia subjek 18 - 60 tahun, maka subjek adalah 'Dewasa'
    elif input >=18 and input < 60:
        print ("\nSubject Dewasa!\n")
    #Jika usia subjek diatas 60 tahun, maka subjek adalah 'Lansia'
    elif input > 60 and input < 100:
        print ("\nSubject Lansia!\n")
    #Jika usia di bawah 0 atau bilangan bulat negative, maka 'Salah Input!'
    else:
        print ("\nSalah input atau usia tidak mungkin di atas 100 tahun!\n") #\n -> new line -> baris baru

input = input('Masukkan usia : ') #prompt
alat_pendeteksi_kategori_golongan_usia(int(input))