import hashlib
import time

class ProofOfStake:
    def __init__(self):
        self.stakers = {}  # Dictionary to hold staker addresses and their stakes

    def stake(self, address, amount):
        """Allows a user to stake a certain amount of coins."""
        if address in self.stakers:
            self.stakers[address] += amount
        else:
            self.stakers[address] = amount

    def get_total_stake(self):
        """Returns the total stake in the network."""
        return sum(self.stakers.values())

    def select_validator(self):
        """Selects a validator based on their stake."""
        total_stake = self.get_total_stake()
        if total_stake == 0:
            return None  # No validators available

        # Randomly select a validator based on their stake
        random_value = random.uniform(0, total_stake)
        cumulative = 0

        for address, stake in self.stakers.items():
            cumulative += stake
            if cumulative >= random_value:
                return address

    def validate_block(self, block, validator):
        """Validates a block proposed by a validator."""
        # Implement block validation logic (e.g., checking previous hash, transactions)
        # For simplicity, we assume the block is valid if it comes from a selected validator
        return block['validator'] == validator

    def get_stakers(self):
        """Returns the list of stakers."""
        return self.stakers
