def jumlahkan(num_1: int, num_2: int = 10)  -> int:
    return num_1 + num_2

#testing1
# print(jumlahkan(5))      # Output: 15 (5 + 10)
# print(jumlahkan(5, 3))   # Output: 8 (5 + 3)

class Angka:
    def __init__(self, number):
        self.number = number

    def add_new(self, other_num):
        self.number = jumlahkan(self.number, other_num)

#testing2
# angka = Angka(10)
# print(angka.number)
# # Output: 10
# angka.add_new(5)
# print(angka.number)
# # Output: 15