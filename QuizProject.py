#LIST PERTANYAAN UNTUK QUIZ BERUPA TIPE DATA DICTIONARY

quiz = {
    "pertanyaan ke 1": {
        "pertanyaan:": "Kapan negara Indonesia merdeka?",
        "pilihan":"A.1945 B.1942 C.1932 D.1998",
        "penjelasan":"Negara Indonesia merdeka pada tanggal 17 Agustus 1945 setelah Ir.Soekarno dan Mohammad Hatta memproklamasikan kemerdekaan Indonesia di Jakarta.",
        "jawaban":"A.1945"
    },"pertanyaan ke 2": {
        "pertanyaan:": "Dimana letak Ibukota negara Indonesia?",
        "pilihan": "A.Surabaya B.DKI Jakarta C.DI Yogyakarta D.Bali",
        "jawaban": "B.DKI Jakarta",
        "penjelasan": "pemilihan Ibukota DKI Jakarta memiliki sejarah dan pertimbangan tertentu, seperti pertimbangan geografis, pertimbangan politis dan ekonomis, warisan kolonial, dan infrastruktur dan fasilitas"
    },"pertanyaan ke 3": {
        "pertanyaan:": "Siapa Presiden pertama Republik Indonesia",
        "pilihan": "A.Ir.Soekarno B.Soeharto C.Jokowi D.BJ Habibie",
        "jawaban": "A.Ir.Soekarno",
        "penjelasan": "Ir.Soekarno memiliki peran penting dalam masa perjuangan kemerdekaan Indonesia sekaligus menjadi bapak proklamator"
    },"pertanyaan ke 4": {
        "pertanyaan:": "Saat ini berapa jumlah provinsi di Indonesia?",
        "pilihan": "A.34 B.32 C.38 D.48",
        "jawaban": "C.38",
        "penjelasan": "adanya pemekaran yang terjadi di Papua dengan menambahkan empat provinsi baru yaitu Provinsi Papua Selatan, Provinsi Papua Tengah, Provinsi Papua Pegunungan, dan Provinsi Papua Barat Daya"
    },"pertanyaan ke 5": {
        "pertanyaan:": "Indonesia terletak diantara dua Benua, yaitu Benua Asia dan Benua? ",
        "pilihan": "A.Eropa B.Amerika C.Antartika D.Australia",
        "jawaban": "D.Australia",
        "penjelasan": "Secara geografis, Indonesia terletak diantara dua Benua, yaitu Benua Asia dan Benua Australia"
    }
}

skor = 0


#PEMBUKAAN QUIZ

print("Selamat Datang di Quiz Indonesia!")
print("")
print("Silahkan pilih salah satu jawaban yang tepat dengan input yang lengkap!")
print("")

#FUNGSI UNTUK MENAMPILKAN PERTANYAAN DAN PILIHAN JAWABAN

for key, value in quiz.items():
    print(value["pertanyaan:"])
    print(value["pilihan"])
    jawaban = input("jawaban?....") #<--FUNGSI UNTUK MEMINTA PENGGUNA MENG-INPUT JAWABAN

#FUNGSI UNTUK MENGHITUNG APABILA JAWABAN BENAR

    if jawaban.lower() == value["jawaban"].lower(): 
        print("Kamu Benar! :)")
        skor = skor + 1
        print("Skor kamu sekarang adalah " + str(skor))
        print("")
        print("")
    
#FUNGSI UNTUK MENGHITUNG APABILA JAWABAN SALAH

    else:
        print("Kamu salah, Nice Try! :(")
        print("Jawaban yang tepat adalah " + value["jawaban"] + " alasannya karena " + value["penjelasan"])
        print("Skor kamu sekarang adalah " + str(skor))
        print("")
        print("---------------------------------")
        print("")


#FUNGSI UNTUK MENGHITUNG TOTAL PEROLEHAN SKOR AKHIR QUIZ

print("Total perolehan skor kamu adalah " + str(skor) + " dari keseluruhan 5 soal")
print("Presentase skormu adalah " + (str(int(skor/5 * 100))) + "%")
print("")
print("")
print("Terima kasih telah mengisi quiz ini, semoga menambah wawasan anda! :)")
