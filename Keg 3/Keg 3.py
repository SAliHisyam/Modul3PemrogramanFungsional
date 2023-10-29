random_list = [105, 3.1, "Hello", 737, "Python", 2.7, "World", 412, 5.5, "AI"]

# Memisahkan elemen-elemen berdasarkan jenis datanya menggunakan map() dan filter()
data_float = list(filter(lambda x: isinstance(x, float), random_list))
data_int = list(filter(lambda x: isinstance(x, int), random_list))
data_string = list(filter(lambda x: isinstance(x, str), random_list))

# Membuat fungsi untuk mengelompokkan angka dalam "Data Int" ke dalam ratusan, puluhan, dan satuan


def categorize_int(number):
    ratusan = number // 100
    puluhan = (number // 10) % 10
    satuan = number % 10
    return {'ratusan': ratusan, 'puluhan': puluhan, 'satuan': satuan}


# Menggunakan map() untuk mengelompokkan angka dalam "Data Int"
categorized_data_int = list(map(categorize_int, data_int))

# Output sesuai dengan format yang diinginkan
print("Data Float:", tuple(data_float))
print("Data Int:")
for item in categorized_data_int:
    print(item)
print("Data String:", data_string)
