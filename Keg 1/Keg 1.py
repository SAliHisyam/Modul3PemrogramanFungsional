def konversi_menit(minggu):
    def konversi_hari(hari):
        def konversi_jam(jam):
            def konversi_menit(menit):
                return (minggu * 7 * 24 * 60) + (hari * 24 * 60) + (jam * 60) + menit
            return konversi_menit
        return konversi_jam
    return konversi_hari


data = ["3 Minggu 3 Hari 7 Jam 21 Menit",
        "5 Minggu 5 Hari 8 Jam 11 Menit",
        "7 Minggu 1 Hari 5 Jam 33 Menit"]

output_data = []
for item in data:
    split_item = item.split()
    minggu = int(split_item[0])
    hari = int(split_item[2])
    jam = int(split_item[4])
    menit = int(split_item[6])

    konversi = konversi_menit(minggu)(hari)(jam)(menit)
    output_data.append(konversi)

print(output_data)
