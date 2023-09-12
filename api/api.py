import json


# klasifikasi berdasarkan surah
def quran(urutan):
    with open("api/alquran/{}.json".format(urutan)) as berkas:
        return json.load(berkas)

class Surah:
    def __init__(self, urutan):
        muat = quran(urutan)
        self.data = muat['nomor'], muat['nama'], muat['namaLatin'], muat['jumlahAyat'], muat['tempatTurun'], muat['arti']
        self.ayat = muat['ayat']


# klasifikasi berdasarkan juz
def quranJuz(urutan):
    with open("api/juz_alquran/{}.json".format(urutan)) as berkas:
        return json.load(berkas)

class Juz:
    def __init__(self, urutan: int):
        arab, latin, indo, nomor, datajuz = [], [], [], [], {}
        for k, v in quranJuz(urutan).items():
            for xx in range(v[0], v[1]):
                arab.append(Surah(k).ayat[str(xx)]["teksArab"])

        for k, v in quranJuz(urutan).items():
            for yy in range(v[0], v[1]):
                latin.append(Surah(k).ayat[str(yy)]["teksLatin"])

        for k, v in quranJuz(urutan).items():
            for zz in range(v[0], v[1]):
                indo.append(Surah(k).ayat[str(zz)]["teksIndonesia"])

        for v in quranJuz(urutan).values():
            for i in range(v[0], v[1]):
                nomor.append(i)
        
        for ui in range(len(arab)):
            datajuz[ui] = nomor[ui], arab[ui], latin[ui], indo[ui]
        
        self.data = datajuz

