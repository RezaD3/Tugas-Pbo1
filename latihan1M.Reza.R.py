import psycopg2
#Connect Database
conn = psycopg2.connect(
         host="localhost",
         database="tugas",
         user="reza1",
         password="123")

#Insert Data
def insert_data(conn):
   idmhs = int(input(" Masukan Nomor ID Anda: "))
   nim = input("Masukan NIM Anda: ")
   nama = input("Masukan Nama Anda: ")
   semester = int(input("Asal Semester?: "))
   tahun = int(input("Tahun lahir??: "))
   val = (idmhs,nim,nama,semester,tahun)
   sql = "INSERT INTO mahasiswa (idmhs, nim, nama, semester, tahun) VALUES (%s, %s, %s, %s, %s)"
   cur = conn.cursor()
   cur.execute(sql, val)
   conn.commit()
   print("==================================")
   print("{} DATA TERSIMPAN".format(cur.rowcount))

#Show Data
def show_data(conn):
   cur = conn.cursor()
   sql = "SELECT * FROM mahasiswa"
   cur.execute(sql)
   result = cur.fetchall()

   if cur.rowcount < 0:
      print("==================================")
      print("DATA TIDAK DITEMUKAN")
   else:
      print("==================================")
      print("-{} DATA DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Update Data
def update_data(conn):
   cur = conn.cursor()
   show_data(conn)
   idmhs = input("Pilih ID Mahasiswa: ")
   nim = input("Masukan NIM Mahasiswa yang Baru: ")
   nama = input("Masukan Nama Mahasiswa Yang Baru: ")
   semester = int(input(" semester berapa?: "))
   tahun = int(input("Tahun berapa?: "))
   sql = "UPDATE mahasiswa SET nim=%s, nama=%s, semester=%s, tahun=%s WHERE idmhs=%s"
   val = (nim, nama, semester, tahun, idmhs)
   cur.execute(sql, val)
   conn.commit()
   print("==================================")
   print("{} DATA BERHASIL DI UPDATE".format(cur.rowcount))

#Delete Data
def delete_data(conn):
   cur = conn.cursor()
   show_data(conn)
   idmhs = str(input("Pilih ID Mahasiswa Yang Akan Dihapus: "))
   slc = "SELECT * FROM mahasiswa WHERE idmhs= %s"
   val = (idmhs)
   cur.execute(slc, val)
   con = cur.rowcount
   if (con == 1):
      inp = input("Yakin Mau hapus data ini ?t? (y/t): ")
      if (inp.upper()=="Y"):
         sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
         val = (idmhs)
         cur.execute(sql, val)
         conn.commit()
         print("==================================")
         print("\b{} DATA BERHASIL DIHAPUS cuy".format(cur.rowcount))
      else:
         print(" yahhhh.... data gagal dihapus dihapus deh")
   else:
      print("ID siapa yang kamu maksud? ")
   """sql = "DELETE FROM mahasiswa WHERE idmhs=%s"
   val = (idmhs)
   cur.execute(sql, val)
   conn.commit()
   print("{} Data Berhasil Dihapus".format(cur.rowcount))"""

#Search Data
def search_data(conn):
   cur = conn.cursor()
   keyword = input("Masukin Nim atau nama yang mau dicari?I: ")
   sql = "SELECT * FROM mahasiswa WHERE nim LIKE %s OR nama LIKE %s OR nama LIKE %s OR nama LIKE %s"
   val = ("%{}%".format(keyword), "%{}%".format(keyword.lower()),"%{}%".format(keyword.upper()),"%{}%".format(keyword.title()))
   cur.execute(sql, val)
   result = cur.fetchall()

   if cur.rowcount <= 0:
      print("==================================")
      print("DATA YANG DICARI TIDAK DITEMUKAN")
   else:
      print("==================================")
      print("{} DATA YANG DICARI BERHASIL DITEMUKAN".format(cur.rowcount))
      for data in result:
         print(data)

#Menampilkan Menu
def show_menu(conn):
   
   print(" Selamat datang diforum perkumpulan mahasiswa UMC")
   print ( "------------------------------------------------")
   print ( "------------------------------------------------")
   print("1. Masukan Data")
   print("2. Tampilkan Data")
   print("3. Perbarui Data")  
   print("4. Hapus Data")
   print("5. Menacari Data")
   print("0. Keluar")
   print("____________________________________________")
   menu = input(" ayo Pilih Menunya kawan?: ")

   if menu == "1":
      insert_data(conn)
   elif menu == "2":
      show_data(conn)
   elif menu == "3":
      update_data(conn)
   elif menu == "4":
      delete_data(conn)
   elif menu == "5":
      search_data(conn)
   elif menu == "0":
      exit()
   else:
      print("Menu salah")

#Looping
if __name__ == "__main__":
   while(True):
      show_menu(conn)