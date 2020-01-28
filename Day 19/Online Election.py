class TopVotedCandidate:
    def __init__(self, persons:List[int], times:List[int]):
        self.times=times
        self.persons=persons
    def q(self, t:int)->int: