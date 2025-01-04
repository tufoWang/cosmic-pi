from web3 import Web3
import json

class ContractManager:
    def __init__(self, web3_provider, contract_address, abi_file):
        self.web3 = Web3(Web3.HTTPProvider(web3_provider))
        self.contract_address = contract_address
        self.abi = self.load_abi(abi_file)
        self.contract = self.web3.eth.contract(address=self.contract_address, abi=self.abi)

    def load_abi(self, abi_file):
        with open(abi_file, 'r') as file:
            return json.load(file)

    def get_balance(self, address):
        return self.contract.functions.balanceOf(address).call()

    def transfer_tokens(self, from_address, to_address, amount, private_key):
        nonce = self.web3.eth.getTransactionCount(from_address)
        transaction = self.contract.functions.transfer(to_address, amount).buildTransaction({
            'chainId': 1,  # Mainnet
            'gas': 2000000,
            'gasPrice': self.web3.toWei('50', 'gwei'),
            'nonce': nonce,
        })

        signed_txn = self.web3.eth.account.signTransaction(transaction, private_key=private_key)
        txn_hash = self.web3.eth.sendRawTransaction(signed_txn.rawTransaction)
        return txn_hash.hex()

    def get_contract_info(self):
        return {
            'address': self.contract_address,
            'name': self.contract.functions.name().call(),
            'totalSupply': self.contract.functions.totalSupply().call(),
        }
