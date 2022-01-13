#Read information from RfidTag(privatekey) and sign transaction with it

import RPi.GPIO as GPIO
from mfrc522 import SimpleMFRC522
import base64
from web3 import Web3
import time



bsc = 'https://speedy-nodes-nyc.moralis.io/++++++++++++++++/eth/goerli'   #connect to node for example moralis.io
web3 = Web3(Web3.HTTPProvider(bsc))
print(web3.isConnected())
reader = SimpleMFRC522()


senderPublic =web3.toChecksumAddress('')
to = web3.toChecksumAddress('')
amountToTransfer = 0.01


def transaction():

    
    nonce = web3.eth.getTransactionCount(senderPublic)

    #build a transaction in a dictionary
    tx = {
        'chainId':5,
        'nonce': nonce,
        'to': to,
        'value': web3.toWei(amountToTransfer, 'ether'),
        'gasPrice': web3.toWei('5', 'gwei'),
        'gas': 210000
    }
    
    time.sleep(5)
    #sign the transaction
    signed_tx = web3.eth.account.sign_transaction(tx,dec)

    #send transaction
    tx_hash = web3.eth.sendRawTransaction(signed_tx.rawTransaction)

    #get transaction hash
    print(web3.toHex(tx_hash))
    print(f'transaction has been sent to {to}')



try:
        print('read from card')
        id, text = reader.read()
        print(id)
        dec = base64.b64decode(text).hex()
        print(dec)
        transaction()
finally:
        GPIO.cleanup()
