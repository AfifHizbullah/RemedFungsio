import matplotlib.pyplot as plt

data_transaksi = [
    ("Produk A", 50, 10),
    ("Produk B", 30, 25),
    ("Produk C", 20, 30),
    ("Produk D", 60, 8),
    ("Produk E", 40, 15),
    ("Produk F", 70, 5),
]

harga_produk = [harga for _, harga, _ in data_transaksi]
jumlah_terjual = [jumlah for _, _, jumlah in data_transaksi]

# Scatter plot
plt.figure(figsize=(10, 6))
plt.scatter(harga_produk, jumlah_terjual, color='blue', marker='o')
plt.title('Hubungan Antara Harga dan Jumlah Produk Terjual')
plt.xlabel('Harga Produk')
plt.ylabel('Jumlah Produk Terjual')

pendapatan_produk = list(map(lambda x: x[1] * x[2], data_transaksi))

# Bar chart
plt.figure(figsize=(10, 6))
produk_names = [produk for produk, _, _ in data_transaksi]
plt.bar(produk_names, pendapatan_produk, color='aqua')
plt.title('Pendapatan Produk')
plt.xlabel('Nama Produk')
plt.ylabel('Pendapatan')

plt.show()
