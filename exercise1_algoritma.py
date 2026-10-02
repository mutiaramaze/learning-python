# # ============
# # soal 1
# # beli telur 5kg
# # harga sekilo 26.000
# # transport 3500 sekali jalan, ibu pp
# # sisa uang ibu jika ibu membawa uang 200.000
telur = 5 * 26000
print("harga telur:", telur)
transport = 3500 * 2
print("transport:", transport)
print("total:", telur + transport)
sisa = (200000 - (telur + transport))
print("sisa uang:", sisa)

# ===============
# soal 2
harga_perkg = 20000
berat_beli = 8
bayar = harga_perkg * berat_beli
print("harga yang dibayar:", bayar)

tugas = 90
presentasi = 75
rerata = (tugas + presentasi) / 2

if tugas >= 85 and presentasi >= 80 and rerata >= 82.5:
    status = "lulus"
else:
    status = "tidak lulus"
print("nilai tugas      :", tugas)
print("nilai presentasi :", presentasi)
print("nilai rerata     :", rerata)
print("status           :", status)