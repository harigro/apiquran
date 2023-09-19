# api-quran
api-quran adalah antarmuka pemrograman aplikasi al-quran berisi informasi surah, 
terjemahan ayat dalam bahasa latin, dan terjemahan dalam 
bahasa indonesia. Antarmuka pemrograman aplikasi ini adalah 
versi pendek dari basis data [alquran](https://github.com/harigro/basis_data).

## Cara Menggunkan api
kode dibawah ini sama dengan kode program pada **main.py**
```python
from api import Surah, Juz
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

def data_juz(nomor_urut: int):
    return Juz(nomor_urut).data

if __name__ == '__main__': 
    print(aa.data)
    data_ayat()
    print(data_juz(1))
```
