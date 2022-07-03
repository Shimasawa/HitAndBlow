# HitAndBlow
Hit&amp;Blowが簡単に作れるライブラリ
# How To Use
```python
#インポート
from hitandblow import HitAndBlow
#予想
num = "半角数字三桁の文字列"
#一ゲームにつき一つインスタンスを作成
hab = HitAndBlow()
#予想した数字を判定
hab.num_check(num)

#取得できる値
#hab.NUM = 当てる数
#hab.turn = ターン数(1始まり)
#hab.hit,hab.blow = hitやblowの数
```
詳しくは`sample.py`から読み取ってください。
