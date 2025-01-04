import random

class DelegatedProofOfStake:
    def __init__(self):
        self.delegates = {}  # Dictionary to hold delegate addresses and their votes
        self.voters = {}     # Dictionary to hold voter addresses and their stakes

    def delegate(self, voter_address, delegate_address, amount):
        """Allows a voter to delegate their stake to a delegate."""
        if voter_address in self.voters:
            self.voters[voter_address] += amount
        else:
            self.voters[voter_address] = amount

        if delegate_address in self.delegates:
            self.delegates[delegate_address] += amount
        else:
            self.delegates[delegate_address] = amount

    def select_delegates(self, num_delegates):
        """Selects a number of delegates based on their total votes."""
        total_votes = sum(self.delegates.values())
        if total_votes == 0:
            return []  # No delegates available

        selected_delegates = []
        for _ in range(num_delegates):
            random_value = random.uniform(0, total_votes)
            cumulative = 0

            for address, votes in self.delegates.items():
                cumulative += votes
                if cumulative >= random_value:
                    selected_delegates.append(address)
                    break

        return selected_delegates

    def validate_block(self, block, delegates):
        """Validates a block proposed by selected delegates."""
        # Implement block validation logic (e.g., checking previous hash, transactions)
        # For simplicity, we assume the block is valid if it comes from one of the selected delegates
        return block['validator'] in delegates

    def get_delegates(self):
        """Returns the list of delegates and their votes."""
        return self.delegates
