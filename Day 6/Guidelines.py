#Hands On
#membuat kode untuk menghitung rata rata dan mencari bilangan terbesar dari sebuah list

# def hitung_rata_rata(daftar):
#     if len(daftar) == 0:
#         return 0  # Jika daftar kosong, rata-ratanya adalah 0
#     else:
#         total = sum(daftar)
#         rata_rata = total / len(daftar)
#         return rata_rata

# # Contoh penggunaan:
# my_list = [1, 2, 3, 4, 5]
# rata_rata = hitung_rata_rata(my_list)
# print("Rata-rata:", rata_rata)



# def cari_terbesar(daftar):
#     if len(daftar) == 0:
#         return None  # Jika daftar kosong, kembalikan None
#     else:
#         terbesar = max(daftar)
#         return terbesar





def rt(umur):
    if len(umur) == 0:
        return 0, None 
    else: 
        total = sum(umur)
        rtrt = total / len(umur)
        umurTerbesar = max(umur)
        return rtrt, umurTerbesar

my_umur = [16, 19, 20, 38, 49, 34, 76, 99]
rtrt,umurTerbesar = rt(my_umur)
terbesar = umurTerbesar(my_umur)
print("Bilangan terbesar:", terbesar)
print("rata rata umurnya dalah", rtrt)




# def rt(umur):
#     if len(umur) == 0:
#         return 0, None  # Jika daftar umur kosong, rata-rata umur adalah 0, dan terbesar adalah None
#     else:
#         total = sum(umur)
#         rtrt = total / len(umur)
#         umurTerbesar = max(umur)
#         return rtrt, umurTerbesar

# my_umur = [16, 19, 20, 38, 49, 34, 76, 99]
# rtrt, terbesar = rt(my_umur)

# if terbesar is not None:
#     print("Bilangan terbesar:", terbesar)
# else:
#     print("Daftar umur kosong.")

# print("Rata-rata umur:", rtrt)


# mencari rata-rata dan menghitung bilangan terbesar dari sebuah list

MyList = [12, 9, 15, 8 , 18 , 7, 21]
def average(data):
    if not data:
        return None 
    total = sum(data)
    avg = total / len(data)
    return avg

AverageMyList = average(MyList)

print(f"Rata-rata my_list: {AverageMyList}")

# def test(a=10, b=2):
#     return a*b

# print(test(30, 5))

# Menghitung rata-rata
def calculate_avg(list):
    sum = 0
    for element in list:
        sum = sum + element

    return sum/len(list)

print(calculate_avg([1,2,3,4,5]))

# nilai=50

# if nilai > 75:
#     print("Congratulation!")
#     print("Anda lulus!")
# elif nilai > 40 and nilai < 60 :
#     print("Lulus bersyarat")
# else:
#     print("Maaf, coba lagi!")


# computer A 10-20jt
# computer B 15-30jt

# Dictionary
# x = {
#         "name" : "Fajri",
#         "age" : 28,
#         "speed": 15
#     }

# if x['name'] == 'Joko':
#     if x['speed'] == 12:
#         print("Kenceng")
#     elif x['speed'] > 13:
#         print("Ampir kenceng")
# elif x['age'] > 5:
#     print("masuk")
#     if x['speed'] > 3:
#         print("Yes")

# print("disni")

# input = 100

# if input < 10 : print("ok") 
# print("yes")

# x = 10
# if x == 10 \
# and x > 3 \
# and x / 2 ==5:
#     pass

# print("correct") if 100/3 == 50 else print('false')
# list = [1,2,100]
# if 100 in list:print('zz')
# data = 2
# if (data == 2) or data ==15 \
#  or data == 13:
#     print("zz")

# data = 10
# if (data == 10):
#     print("hello")
# elif:
#     print("opsi 2")

number1=1000
data = ['car', 'motor', 'bike']
if 'bike' in data and number1 / 2 == 500: 
    print('zzz')
else: 
    print('wew')

# leetcode.com (buat latihan algoritma/coding)

# Fungsi menghitung nilai terbesar dari list

# i = 0
# while i<10:
#     print("hello -->", i)#i=1
#     i = i + 1
#     #i=2
       #0 1   2  3  4   5
# list = [5, 5, 6, 7, 12, 10]
# # for li in list:
# #     print(li)

# i = 0
# while i < len(list):
#     print(i)
#     i = i + 1

          #0      1    -- 2         3       4 --       5        6
# colors = ['red', 'blue','yellow', 'green', 'black', 'pink', 'yellow']
# # print(colors[2])

# # print(colors.index('yellow'))

# i = 0; c = 0
# for col in colors:
#     if col == 'yellow':
#         c = c + 1
#         if c == 3:
#             print(i)
#     i = i + 1

# some_colors = colors[2 : 5]
# print(some_colors)

# slicing from behind
# some_colors = colors[5 : 2 : -1]
# print(some_colors)

      # 0   1   2  - 3  4   5   6 -  7   8
list = [10, 20, 30, 40, 50, 60, 70, 80, 90]

# list[:] = [0,0,0]

# print(list)

# del list[3:7:2]

# print(list)

list_length = len(list)
mid = list_length//2

print(list[mid])

# Array/list []
# list = [1,2,3,4,5,6,7,8,9,10]
# for li in list:
#     print(li)

# String(text) ""
# text = "BNSP"
# for char in text:
#     print(char)

# SET (for unique element) {}
# set_data = {1, 1, 2, 2, 1}
# for sd in set_data:
#     print(sd)

# Tuple (can't be modified) ()
# tuple_data = (2,3,4,5)
# for td in tuple_data:
#     print(td)

# Dictionary (Mapping key value pair of data)
# dict_data = {
#     "name": "Fajri",
#     "Age": 28,
#     "isFemale": False,
#     "speed": 2.0
# }

# for dd in dict_data:
#     print(dict_data[dd])

a = list(range(1,2,1,4))

print(a)

# print(list[0])
# print(list[1])
# print(list[2])
# print(list[3])
# print(list[4])
# print(list[5])
# print(list[0])
# print(list[0])
# print(list[0])
# print(list[0])