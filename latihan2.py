# Modal awal
modal_awal = 100_000_000  # 100 juta

# Persentase laba per bulan (dalam urutan bulan 1 sampai 8)
persentase_laba = [0, 0, 0.01, 0.01, 0.05, 0.05, 0.05, 0.03]

# Hitung laba tiap bulan
laba_per_bulan = [modal_awal * p for p in persentase_laba]

# Hitung total laba selama 8 bulan
total_laba = sum(laba_per_bulan)

# Tampilkan hasil
print("📊 Rincian Laba per Bulan:")
for i, laba in enumerate(laba_per_bulan, start=1):
    print(f"Bulan {i}: Rp{laba:,.0f}")

print(f"\n💰 Total Keuntungan Selama 8 Bulan: Rp{total_laba:,.0f}")