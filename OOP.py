market_length = 15

class Crypto():
    
    def credit_cards(self):
        print("This currency can be exchanged through microtransaction")
    
    def mining(self):
        print("This currency can be mined")

class Bitcoin(Crypto):
    
    def __init__(self):
        exchange_rate_B = 5
        print(f"the value of Bitcoin in the Crypto market is: {exchange_rate_B * market_length}")

class Etherium(Crypto):

    def __init__(self):
        exchange_rate_E = 2 
        print(f"the value of Etherium coin in the Crypto market is: {exchange_rate_E * market_length}")

class PiCoin(Crypto):

    def __init__(self):
        exchange_rate_PI = 0.2
        print(f"the value of PIcoib in the Crypto market is: {exchange_rate_PI * market_length}")

bitcoin = Bitcoin()
bitcoin.mining()

etherium = Etherium()
etherium.mining()

picoin = PiCoin()
etherium.credit_cards()

