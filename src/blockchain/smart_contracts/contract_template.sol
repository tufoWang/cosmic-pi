// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

contract CosmicPiContract {
    string public name;
    address public owner;
    uint256 public totalSupply;
    uint256 public constant PI_COIN_VALUE = 314159; // Fixed value of Pi Coin in USD

    mapping(address => uint256) public balances;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event ContractCreated(string name, address owner, uint256 totalSupply);

    constructor(string memory _name, uint256 _totalSupply) {
        name = _name;
        owner = msg.sender;
        totalSupply = _totalSupply;
        balances[owner] = totalSupply;
        emit ContractCreated(name, owner, totalSupply);
    }

    // Function to transfer tokens
    function transfer(address _to, uint256 _value) public returns (bool success) {
        require(balances[msg.sender] >= _value, "Insufficient balance");
        require(_to != address(0), "Invalid address");

        balances[msg.sender] -= _value;
        balances[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;
    }

    // Function to check the balance of an address
    function balanceOf(address _owner) public view returns (uint256 balance) {
        return balances[_owner];
    }

    // Function to get the fixed value of Pi Coin in USD
    function getPiCoinValue() public pure returns (uint256) {
        return PI_COIN_VALUE;
    }
}
