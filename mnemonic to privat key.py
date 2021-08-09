from time import time
from datetime import timedelta, datetime
import json
import atexit
import itertools
from hdwallet import BIP44HDWallet
from hdwallet.cryptocurrencies import EthereumMainnet
from eth_keys import keys
import requests
import os    
import time    

colour_cyan = '\033[36m'
colour_reset = '\033[0;0;39m'
colour_red = '\033[31m'
colour_green='\033[0;32m'



d = open('file.json')
j = json.load(d)
p = itertools.permutations(j, 12)
na= 0
no= 0
for val in (p):
    na+=1
    y = (' '.join(val))
    x = str(y)
    
    try:
        bip44_hdwallet: BIP44HDWallet = BIP44HDWallet(cryptocurrency = EthereumMainnet, account = 0, change = False, address = 0)
        mne = str(x)
        bip44_hdwallet.from_mnemonic(mnemonic = mne)
        bib = (bip44_hdwallet.private_key())
        pw = (bib)
        pb = (bib + '\n' + str(x))

        
        key = str(pw)
        
        private_key = key[:64]
        private_key_bytes = bytes.fromhex(private_key)
        public_key_hex = keys.PrivateKey(private_key_bytes).public_key
        public_key_bytes = bytes.fromhex(str(public_key_hex)[2:])
        ethadd = keys.PublicKey(public_key_bytes).to_address()

        ethadd = str(bip44_hdwallet.address())
        bscadd = str(bip44_hdwallet.address())
        eth = requests.get("https://api.etherscan.io/api?module=account&action=balance&address=" + ethadd + "&tag=latest&apikey=GNQBU97R7JCMTW296ZNYICU88M8DGXFNW5")
        bsc = requests.get("https://api.bscscan.com/api?module=account&action=balance&address=" + bscadd + "&tag=latest&apikey=9D9NV986GXPHCUBHAAHAKGTYGYR2ZK25NM")
        ht = requests.get("https://api.hecoinfo.com/api?module=account&action=balance&address=" + bscadd + "&tag=latest&apikey=WAWRUF8Y3A42HA19C78GFDVXHMP4DHRWN3")
        polygon = requests.get("https://api.polygonscan.com/api?module=account&action=balance&address=" + bscadd + "&tag=latest&apikey=NPK2G58QQ2GPSCR6C2K6XVC84UHD37U2SB")
        
        ress = eth.json()
        balance = dict(ress)["result"]
        ress = bsc.json()
        saldo = dict(ress)["result"]
        ress = ht.json()
        hts = dict(ress)["result"]
        ress = polygon.json()
        polygons = dict(ress)["result"]
        
        
        print ("\n " + colour_cyan +"Scan : " +  str (no) + colour_green + '\n >>>>>>>>>>>>>>>>>>>>' + colour_reset + '\n Bsc   balance : ' +  str(saldo) + '\n Eth   balance : ' +  str(balance) + '\n Ht    balance : ' +  str(hts) + '\n Matic balance : ' +  str(polygons) + colour_green + '\n >>>>>>>>>>>>>>>>>>>>' )
        
        print(colour_cyan + " Eth address : " + colour_cyan + ethadd + colour_cyan +'\n PrivateKey' + '  : ' + colour_cyan + pw +'\n Mnemonic' + '    : ' + colour_cyan + x)
        print("----------------------")
        no = no + 1
        if int(balance) > 0:
            f=open(u"eth.txt","a")
            f.write('\n Eth Address: ' + ethadd)
            f.write('\nPrivateKey (hex): ' + key)
            f.write('\n---------------------------')
            f.close()
            
        if int(saldo) > 0:
            f=open(u"bsc.txt","a")
            f.write('\n Bsc Address: ' + bscadd)
            f.write('\nPrivateKey (hex): ' + key)
            f.write('\n---------------------------')
            f.close()
        if int(hts) > 0:
            f=open(u"Ht.txt","a")
            f.write('\n Ht Address: ' + ethadd)
            f.write('\nPrivateKey (hex): ' + key)
            f.write('\n---------------------------')
            f.close()
            
        if int(polygons) > 0:
            f=open(u"Matic.txt","a")
            f.write('\n Matic Address: ' + bscadd)
            f.write('\nPrivateKey (hex): ' + key)
            f.write('\n---------------------------')
            f.close()

        print(colour_red + "\n Mnemonic does not exist " + colour_red +"Erorrr : " + colour_cyan + str (na)  +  " Next" + colour_reset)
            
    except:
        
        stop = ("= ")
        if stop == '':
            break
        



