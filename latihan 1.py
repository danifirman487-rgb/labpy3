import random

# Meminta input dari pengguna
n = int(input("Masukkan jumlah bilangan acak yang ingin ditampilkan (< 0.5): "))

# Inisialisasi penghitung dan daftar hasil
count = 0
hasil = []

# Gunakan while untuk mengulang sampai jumlah n terpenuhi
while count < n:
    bilangan = random.random()  # Menghasilkan bilangan acak antara 0 dan 1
    if bilangan < 0.5:
        hasil.append(bilangan)
        count += 1

# Tampilkan hasil menggunakan for
print(f"\n{n} bilangan acak yang kurang dari 0.5:")
for i, angka in enumerate(hasil, start=1):
    print(f"{i}. {angka:.8f}")