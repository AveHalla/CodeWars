class User:
    rank_vector: list[int] = [i for i in range(-8, 9) if i != 0]

    def __init__(self):
        self.rank: int = -8
        self.progress: int = 0

    def inc_progress(self, kata: int) -> int:
        if kata not in self.rank_vector:
            raise ValueError('Not in the specified Range of features')
        if self.rank == 8:
            progressmeter: int = 0
        elif self.rank_vector.index(kata) == self.rank_vector.index(self.rank):
            progressmeter: int = self.progress + 3
        elif self.rank_vector.index(kata) == self.rank_vector.index(self.rank) - 1:
            progressmeter: int = self.progress + 1
        elif self.rank_vector.index(kata) <= self.rank_vector.index(self.rank) - 2:
            progressmeter: int = self.progress
        elif self.rank == -1 and kata == 1:
            progressmeter: int = self.progress + 10
        else:
            progressmeter: int = self.progress + 10 * pow(
                abs(self.rank_vector.index(kata) - self.rank_vector.index(self.rank)), 2)
        progressindex: list[int] = list(divmod(progressmeter, 100))
        self.progress = progressindex[1]
        self.rank = self.updaterank(progressindex[0])
        if self.rank == 8:
            self.progress = 0
        return self.progress

    def updaterank(self, level=1) -> int:
        if self.rank == 8:
            return self.rank
        elif self.rank_vector.index(self.rank) + level > self.rank_vector.index(8):
            self.rank = 8
        else:
            self.rank = self.rank_vector[self.rank_vector.index(self.rank) + level]
        return self.rank
