from hitandblow import HitAndBlow

def input_check(num :str) -> bool:
    return not (len(num) == 3 and num.isdecimal())

hab = HitAndBlow()
while(1):
    num = input(f"{hab.turn}回目\n半角数字三桁を入力 : ")
    if input_check(num):
        print("入力が正しくありません")
        continue
    hab.check(num)
    if hab.hit == 3:
        input(f"{hab.turn}回目で正解しました\n答え : {hab.NUM}")
        break
    else:
        print(f"hit : {hab.hit}, blow : {hab.blow}")
    if hab.turn == 10:
        input(f"10回以内に正解にたどり着けませんでした\n正解 : {hab.NUM}")
        break
    