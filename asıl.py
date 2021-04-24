import urllib.request
import json
import pandas as pd


with urllib.request.urlopen("https://security-9c7bc.firebaseio.com/Ayl%C4%B1k%20Tamamlanan%20G%C3%BCn%20Say%C4%B1lar%C4%B1/2021/Mar.json") as url:
        data = json.loads(url.read().decode())
        df = pd.DataFrame(data)
        df1 = df.stack().swaplevel()
        print(df1)
        df1.to_csv("cıktı.csv")

