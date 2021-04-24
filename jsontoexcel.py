
import urllib.request
import json
import pandas as pd


def aylar (ay):
    sonay = ""
    if ay == "Ocak" or ay == "ocak":
        sonay = "Oca"

    elif ay == "Şubat" or ay == "şubat":
        sonay = "Şub"

    elif ay == "Mart" or ay == "mart":
        sonay = "Mar"

    elif ay == "Nisan" or ay == "nisan":
        sonay = "Nis"

    elif ay == "Mayıs" or ay == "mayıs":
        sonay = "May"

    elif ay == "Haziran" or ay == "haziran":
        sonay = "Haz"

    elif ay == "Temmuz" or ay == "temmuz":
        sonay = "Tem"

    elif ay == "Ağustos" or ay == "ağustos":
        sonay = "Ağu"

    elif ay == "Eylül" or ay == "eylül":
        sonay = "Eyl"

    elif ay == "Ekim" or ay == "ekim":
        sonay = "Eki"

    elif ay == "Kasım" or ay == "kasım":
        sonay = "Kas"

    elif ay == "Aralık" or ay == "aralık":
        sonay = "Ara"

    else:
        print("Lütfen ay ismini kontrol ediniz")

    with urllib.request.urlopen(
            "https://security-9c7bc.firebaseio.com/Ayl%C4%B1k%20Tamamlanan%20G%C3%BCn%20Say%C4%B1lar%C4%B1/2021/"+ sonay +".json") as url:
        data = json.loads(url.read().decode())
        df = pd.DataFrame(data)
        df1 = df.stack().swaplevel()
        df1.to_csv(sonay + ".csv", encoding="utf-8")


if __name__ == '__main__':
    while True:
        giris = input("Ay Giriniz")
        aylar(giris)











