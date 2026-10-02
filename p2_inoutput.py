# print("="*30)
# print("="*10 + "DATA DIRI MAHASISWA" + "="*10)
# print("="*30)

# nim = input("NIM                    :")
# nama = input("Nama                  :")
# jurusan = input("Jurusan            :")
# alamat = input("Alamat              :")
# nilai1 = int(input("Input nilai 1   :"))
# nilai2 = int(input("Input nilai 2   :"))

# print("="*30)
# print("="*10 +  "HASIL CETAK DATA DI ATAS" +  "="*10)
# print("="*30)

# print("NIM anda adalah      :" +str(nim))
# print("Nama anda adalah     :" +str(nama))
# print("Jurusan anda adalah  :" +str(jurusan))
# print("Alamat anda adalah   :" +str(alamat))
# print("="*30)
# print("Hasil perkalian      :" +str(nilai1 * nilai2))
# print("Hasil pembagian      :" +str(nilai1 / nilai2))
# print("Hasil pertambahan    :" +str(nilai1 + nilai2))
# print("Hasil pengurangan    :" +str(nilai1 - nilai2))
# print("="*30)



print("="*30)
print("="*10 + "DATA DIRI MAHASISWA" + "="*10)
print("="*30)

#input datanya di terminal
nim = input("NIM                    :")
nama = input("Nama                  :")
jurusan = input("Jurusan            :")
alamat = input("Alamat              :")
nilai1 = int(input("Input nilai 1   :"))
nilai2 = int(input("Input nilai 2   :"))

#proses perhitungannya tapi ga masuk di outputnya nanti
kali = nilai1 * nilai2
bagi = nilai1 / nilai2
kurang = nilai1 - nilai2
tambah = nilai1 + nilai2

print("="*30)
print("="*10 +  "HASIL CETAK DATA DI ATAS" +  "="*10)
print("="*30)

#outputnya
print("NIM anda adalah      :" +str(nim))
print("Nama anda adalah     :" +str(nama))
print("Jurusan anda adalah  :" +str(jurusan))
print("Alamat anda adalah   :" +str(alamat))

print("="*30)

print("Hasil perkalian      :" +str(kali)) #harus string biar kebaca
print("Hasil pembagian      :" +str(bagi))
print("Hasil pertambahan    :" +str(tambah))
print("Hasil pengurangan    :" +str(kurang))
print("="*30)


