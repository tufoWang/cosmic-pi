class Governance:
    def ```python
    __init__(self):
        self.proposals = []
        self.votes = {}

    def create_proposal(self, proposal):
        self.proposals.append(proposal)
        self.votes[proposal] = {'for': 0, 'against': 0}

    def vote(self, proposal, vote):
        if proposal not in self.proposals:
            raise Exception("Proposal does not exist")
        if vote not in ['for', 'against']:
            raise Exception("Invalid vote option")

        self.votes[proposal][vote] += 1

    def get_results(self, proposal):
        if proposal not in self.proposals:
            raise Exception("Proposal does not exist")
        return self.votes[proposal]

    def execute_proposal(self, proposal):
        if proposal not in self.proposals:
            raise Exception("Proposal does not exist")
        results = self.get_results(proposal)
        if results['for'] > results['against']:
            return f"Proposal '{proposal}' executed successfully."
        else:
            return f"Proposal '{proposal}' was rejected."
