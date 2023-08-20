from api import Surah
import pprint


# ambil surah berdasarkan urutannya di alquran
aa = Surah(1)

# data_surah akan mengembalikan data surah berupa
# nomor, nama, nama latin, jumlah ayat, tempat turun, dan arti
def data_surah():
    return aa.data


def data_ayat():
    jumlah_ayat = data_surah()[3]
    for i in range(jumlah_ayat):
        print(aa.ayat[str(i+1)]['teksArab'])
        print(aa.ayat[str(i+1)]['teksLatin'])
        print(aa.ayat[str(i+1)]['teksIndonesia'])
        print()

if __name__ == '__main__': 
    print(aa.data)
    data_ayat()