import tkinter as tk  # Mengimpor pustaka Tkinter sebagai `tk` untuk membangun GUI
from tkinter import messagebox  # Mengimpor `messagebox` untuk menampilkan pesan error kepada pengguna

# Fungsi untuk menghitung hasil prediksi berdasarkan input nilai mata pelajaran
def hasil_prediksi():
    try:
        total_nilai = 0  # Variabel untuk menjumlahkan total nilai
        for entry in entries:
            # Mengambil nilai dari setiap input entry
            nilai = int(entry.get())  # Mengonversi nilai dari teks ke integer
            # Memastikan nilai berada di antara 0 dan 100
            if not (0 <= nilai <= 100):
                raise ValueError("Nilai harus antara 0 dan 100.")
            total_nilai += nilai  # Menambahkan nilai ke total

        # Menghitung rata-rata nilai
        rata_rata = total_nilai / len(entries)
        
        # Menentukan prodi berdasarkan rata-rata nilai
        if rata_rata >= 80:
            prodi = "Teknologi Informasi"
        elif 60 <= rata_rata < 80:
            prodi = "Pendidikan Bahasa"
        elif 50 <= rata_rata < 60:
            prodi = "Pertanian"
        else:
            prodi = "Tidak ada prodi yang cocok"
        
        # Menampilkan hasil prediksi di label hasil
        hasil_label.config(text=f"Prediksi Prodi: {prodi} (Rata-rata: {rata_rata:.2f})")
        
    except ValueError as ve:
        # Menampilkan pesan error jika input tidak valid (misalnya bukan angka atau di luar rentang 0-100)
        messagebox.showerror("Input Error", "Pastikan semua input adalah angka antara 0 dan 100.")

# Membuat jendela utama aplikasi Tkinter
root = tk.Tk()
root.title("Aplikasi Prediksi Prodi Pilihan")  # Menetapkan judul jendela
root.geometry("500x600")  # Mengatur ukuran jendela
root.configure(bg="#f0f0f0")  # Mengatur warna latar belakang jendela utama

# Membuat label judul di bagian atas aplikasi
judul_label = tk.Label(
    root,  # Menempatkan label ini dalam jendela utama
    text="Aplikasi Prediksi Prodi Pilihan",  # Teks yang ditampilkan
    font=("Arial", 18, "bold"),  # Menetapkan font, ukuran, dan gaya teks
    bg="#f0f0f0"  # Mengatur warna latar belakang sesuai dengan warna jendela
)
judul_label.pack(pady=20)  # Menempatkan label dengan jarak vertikal 20 piksel

# Membuat frame untuk mengelompokkan input nilai mata pelajaran
frame_input = tk.Frame(root, bg="#f0f0f0")  # Mengatur warna latar belakang frame
frame_input.pack(pady=10)  # Menempatkan frame dengan jarak vertikal 10 piksel

# Membuat daftar entries untuk menampung widget input (Entry) untuk setiap nilai mata pelajaran
entries = []
for i in range(10):  # Loop untuk membuat 10 input nilai mata pelajaran
    # Label untuk setiap mata pelajaran, misalnya "Nilai Mata Pelajaran 1:"
    label = tk.Label(
        frame_input,  # Menempatkan label ini dalam `frame_input`
        text=f"Nilai Mata Pelajaran {i + 1}:",  # Menampilkan nomor mata pelajaran
        font=("Arial", 12),  # Menetapkan font dan ukuran teks
        bg="#f0f0f0"  # Mengatur warna latar belakang label
    )
    label.grid(row=i, column=0, padx=10, pady=5, sticky="e")  
    # Menempatkan label pada baris `i`, kolom 0 dengan padding dan rata kanan
    
    # Membuat input (Entry) untuk setiap nilai mata pelajaran
    entry = tk.Entry(frame_input, width=10, font=("Arial", 12))  # Ukuran input ditetapkan ke 10 karakter
    entry.grid(row=i, column=1, padx=10, pady=5)  # Menempatkan entry di kolom sebelah label
    entries.append(entry)  # Menyimpan setiap `entry` dalam daftar `entries`

# Membuat tombol untuk menampilkan hasil prediksi
prediksi_button = tk.Button(
    root,  # Menempatkan tombol ini dalam jendela utama
    text="Hasil Prediksi",  # Teks pada tombol
    command=hasil_prediksi,  # Fungsi yang akan dipanggil saat tombol ditekan
    font=("Arial", 12, "bold"),  # Menetapkan font, ukuran, dan gaya teks
    bg="#4CAF50",  # Mengatur warna latar belakang tombol
    fg="black"  # Mengatur warna teks tombol
)
prediksi_button.pack(pady=30)  # Menempatkan tombol dengan jarak vertikal 30 piksel

# Membuat label untuk menampilkan hasil prediksi
hasil_label = tk.Label(
    root,  # Menempatkan label ini dalam jendela utama
    text="",  # Teks awal kosong; akan diubah saat tombol ditekan
    font=("Arial", 14, "italic", "bold"),  # Menetapkan font, ukuran, dan gaya teks
    fg="blue",  # Mengatur warna teks
    bg="#f0f0f0"  # Mengatur warna latar belakang
)
hasil_label.pack(pady=20)  # Menempatkan label hasil dengan jarak vertikal 20 piksel

# Menjalankan aplikasi
root.mainloop()
