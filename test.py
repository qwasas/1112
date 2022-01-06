import pyupbit

access = "eTxvxmzlaILMWSx7KY6HpLDAp70isWMrxYKeY2ja"          # 본인 값으로 변경
secret = "nXLyxbUaYv46aGYGE44XWjSNAOmvxLfR1nkE2pKe"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회