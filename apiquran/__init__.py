from api import Surah, Juz
import pprint, time


# menampilkan berdasarkan surah
def tampilkan(surah_quran: Surah):
    jumlah_ayat = surah_quran.data[1]
    for i in range(len(jumlah_ayat)):
        print(aa.ayat[str(i+1)]['teksArab'])
        print(aa.ayat[str(i+1)]['teksLatin'])
        print(aa.ayat[str(i+1)]['teksIndonesia'])
        print()


# menampilkan berdasarkan ayat
def data_juz(nomor_urut: int):
    return Juz(nomor_urut).data

if __name__ == '__main__': 
    # aa = Surah(1)
    # tampilkan(aa)
    # -0.0007712930000707274

    satu = time.time()
    jz = Juz(1)
    pprint.pprint(jz.data, sort_dicts=False)
    dua = time.time()
    print(dua-satu)
