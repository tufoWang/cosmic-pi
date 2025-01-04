// scripts/web3.js

import Web3 from 'web3';

let web3;

async function initWeb3() {
    if (window.ethereum) {
        web3 = new Web3(window.ethereum);
        try {
            await window.ethereum.request({ method: 'eth_requestAccounts' });
        } catch (error) {
            console.error('User  denied account access');
        }
    } else {
        console.error('No Ethereum browser detected. Install MetaMask.');
    }
}

async function getAccount() {
    const accounts = await web3.eth.getAccounts();
    return accounts[0];
}

async function sendTransaction(transaction) {
    const account = await getAccount();
    return await web3.eth.sendTransaction({
        from: account,
        to: transaction.recipient,
        value: web3.utils.toWei(transaction.amount.toString(), 'ether')
    });
}

export { initWeb3, getAccount, sendTransaction };
