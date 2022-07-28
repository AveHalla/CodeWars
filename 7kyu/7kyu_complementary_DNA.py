def dna_strand(dna: str) -> str:
    complements: dict[str:str] = {
        'A': 'T',
        'T': 'A',
        'G': 'C',
        'C': 'G',
    }
    return ''.join(complements[x] for x in dna)
