total = 50
accepted_values = {5,10,25}
print(f"Amount Due:  {total}")
while(total > 0):
    coin_value=int(input("Insert Coin: "))
    if(coin_value in accepted_values):
        total-=coin_value
    if(total>0):
        print(f"Amount Due: {total}\n")
print(f"Change Owed: {-total}\n")
