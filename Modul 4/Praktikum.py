import math

def translasi(tx, ty):
    def transformasi_translasi(x, y):
        return x + tx, y + ty
    return transformasi_translasi

def dilatasi(sx, sy):
    def transformasi_dilatasi(x, y):
        return x * sx, y * sy
    return transformasi_dilatasi

def rotasi(sudut):
    def transformasi_rotasi(x, y):
        radian = math.radians(sudut)
        x_baru = x * math.cos(radian) - y * math.sin(radian)
        y_baru = x * math.sin(radian) + y * math.cos(radian)
        return x_baru, y_baru
    return transformasi_rotasi

def cetak_koordinat(aksi_transformasi, x, y):
    x_baru, y_baru = aksi_transformasi(x, y)
    print(f"Koordinat setelah {aksi_transformasi.__name__}: ({x_baru}, {y_baru})")

def point(x, y):
    return x, y

def line_equation_of(p1, p2):
    def calculate_slope(p1, p2):
        return (p2[1] - p1[1]) / (p2[0] - p1[0])

    def calculate_intercept(p, m):
        return p[1] - m * p[0]

    M = calculate_slope(p1, p2)
    C = calculate_intercept(p1, M)

    return f"y = {M:.2f}x + {C:.2f}"

# TUGAS 1
titik_A_genap = (2, 1)
titik_B_genap = (1, 0)

# TUGAS 2
translasi_aksi = translasi(2, -3)
rotasi_aksi = rotasi(60)
perbesaran_aksi = dilatasi(1.5, 2)

titik_A_genap_transformed = perbesaran_aksi(*rotasi_aksi(*translasi_aksi(*titik_A_genap)))
titik_B_genap_transformed = perbesaran_aksi(*rotasi_aksi(*translasi_aksi(*titik_B_genap)))

# TUGAS 3
persamaan_garis_genap = line_equation_of(point(*titik_A_genap_transformed), point(*titik_B_genap_transformed))

print("\nPersamaan garis sebelum transformasi:")
print(line_equation_of(point(*titik_A_genap), point(*titik_B_genap)))

# Cetak hasil
print("\nPersamaan garis hasil transformasi:")
print(persamaan_garis_genap)
