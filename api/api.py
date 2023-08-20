import json

def quran(urutan):
    with open("api/alquran/{}.json".format(urutan)) as berkas:
        return json.load(berkas)

class Surah(object):
    def __init__(self, urutan):
        muat = quran(urutan)
        self.data = muat['nomor'], muat['nama'], muat['namaLatin'], muat['jumlahAyat'], muat['tempatTurun'], muat['arti']
        self.ayat = muat['ayat']
            
        