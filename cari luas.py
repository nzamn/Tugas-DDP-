pilih = int(input ("cari luas ? 1 untuk persegi, 2 untuk lingkaran, 3 segitiga"))

match pilih:
case 1:
  print(int(input ("berapa sisinya?")) ** 2)
case 2:
  print(3.14 * int(input ("berapa jari jari nya?")) **2)
case 3:
  print(1/2 * int(input("berapa alasnya? ")) * int(input("berapa tingginya?")))
case _:
  print("salah angka")