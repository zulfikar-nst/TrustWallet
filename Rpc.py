from web3 import Web3
import json
import requests

ethadd = ("0x2e3Fc3a1CDA9cfa0E6C86A9fdd6A173bcbae8d1B")

ethurl = "https://main-light.eth.linkpool.io/"
ethurl = "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"
ethurl = "https://mainnet.infura.io/v3/6d1611ee7c604fe788af638a138456c9"
ethurl = "https://mainnet.infura.io/v3/56666a488f594a31bd283bfec1fab0f8"
ethurl = "https://mainnet.infura.io/v3/9aa3d95b3bc440fa88ea12eaa4456161"
ethurl = "https://mainnet.infura.io/v3/0cbd82e4bc4c44249eae016fca892f0e"
ethurl = "https://mainnet.infura.io/v3/c9088eec3e1f402e8a4b1192d940538e"
ethurl = "https://mainnet.infura.io/v3/72e93d9ec3c44a20a00fb4998d7e4be9"
ethurl = "https://mainnet.infura.io/v3/871f50b5794047fc8fa50912d07b20b4"
ethurl = "https://mainnet.infura.io/v3/3c58212300d94c97a2ee2a188ccd4805"
ethurl = "https://mainnet.infura.io/v3/89ad39a2ee084e8cab6a81a0a9f1c6a2"
ethurl = "https://mainnet.infura.io/v3/3728e3904e514adda9553d13d4dd747f"
ethurl = "https://mainnet.infura.io/v3/b509a7d40fb246aa8784763cb1a0ff44"
web3 = Web3(Web3.HTTPProvider(ethurl))
bbalance = web3.eth.getBalance(ethadd)

print(web3.fromWei(bbalance, "ether"))

bscurl = "https://bsc-dataseed.binance.org/"
bscurl = "https://bsc-dataseed1.defibit.io/"
bscurl = "https://bsc-dataseed1.ninicoin.io/"
bscurl = "https://bsc-dataseed2.defibit.io/"
bscurl = "https://bsc-dataseed3.defibit.io/"
bscurl = "https://bsc-dataseed4.defibit.io/"
bscurl = "https://bsc-dataseed2.ninicoin.io/"
bscurl = "https://bsc-dataseed3.ninicoin.io/"
bscurl = "https://bsc-dataseed4.ninicoin.io/"
bscurl = "https://bsc-dataseed1.binance.org/"
bscurl = "https://bsc-dataseed2.binance.org/"
bscurl = "https://bsc-dataseed3.binance.org/"
bscurl = "https://bsc-dataseed4.binance.org/"
web3 = Web3(Web3.HTTPProvider(bscurl))
ssaldo = web3.eth.getBalance(ethadd)

print(web3.fromWei(ssaldo, "ether"))
