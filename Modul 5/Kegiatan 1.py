import matplotlib.pyplot as plt
from functools import reduce

nilai_mahasiswa = [75, 80, 90, 65, 70, 85, 95, 78, 88, 92]

rata_rata = reduce(lambda x, y: x + y, nilai_mahasiswa) / len(nilai_mahasiswa)

label_mahasiswa = list(map(lambda x: f'{x+1}', range(len(nilai_mahasiswa))))

plt.bar(label_mahasiswa, nilai_mahasiswa, color='blue')
plt.xlabel('Mahasiswa')
plt.ylabel('Nilai Ujian')
plt.title('Diagram Batang Nilai Ujian Mahasiswa')
plt.axhline(y=rata_rata, color='red', linestyle='--', label=f'Rata-rata: {rata_rata:.2f}')
plt.legend()

plt.show()
