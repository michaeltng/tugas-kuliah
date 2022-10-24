# Tugas Pyhton
class Person:
    def _init__(self,nama,umur):
        self.nama = nama
        self.umur = umur
    
    def fungsi(self):
        print("Hello, nama saya adalah"+self.nama)

class Dewasa(person):
    def __init__(self,nama,umur,alamat):
        super().__init__(namma,umur)
        self.alamat = alamat


x = dewasa("Michael",26,"Tangerang")
print(x.alamat)


