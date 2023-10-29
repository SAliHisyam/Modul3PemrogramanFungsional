data = ["3 Minggu 3 Hari 7 Jam 21 Menit",
        "5 Minggu, 5 Hari 8 Jam 11 Menit",
        "7 Minggu 1 Hari 5 Jam 33 Menit"]


def filter_integers(text):
    integers = filter(str.isdigit, text.split())
    return list(integers)


filtered_data = list(map(filter_integers, data))

for item in filtered_data:
    print(item)
