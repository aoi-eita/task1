### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース

import csv
import pandas as pd

# 検索ソース
data = pd.read_csv("./kimetu.csv",encoding = "shift-jis")
data = data['name']


### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")

### ここに検索ロジックを書く
    source = list(data)

    if word in source:
        print("{}が見つかりました".format(word))
    
    else:
        print("{}が見つかりませんでした".format(word))
        source.append(word)
        source = pd.DataFrame(source,columns=["name"])
        source.to_csv("./kimetu.csv",encoding="shift-jis")

if __name__ == "__main__":
    search()
