class CKYParser:
    """
    Cocke-Younger-Kasami (CKY) PCFG Parser.
    Computes max-probability parse trees over words.
    """
    def __init__(self, unary_rules, binary_rules):
        self.unary = unary_rules
        self.binary = binary_rules

    def parse(self, words):
        n = len(words)
        table = [[{} for _ in range(n + 1)] for _ in range(n + 1)]
        for i in range(1, n + 1):
            w = words[i - 1]
            for lhs, p in self.unary.get(w, []):
                table[i - 1][i][lhs] = max(table[i - 1][i].get(lhs, 0.0), p)

        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length
                for k in range(i + 1, j):
                    for b_sym, p_b in table[i][k].items():
                        for c_sym, p_c in table[k][j].items():
                            for a_sym, p_a in self.binary.get((b_sym, c_sym), []):
                                prob = p_a * p_b * p_c
                                if prob > table[i][j].get(a_sym, 0.0):
                                    table[i][j][a_sym] = prob
        return table[0][n].get("S", 0.0)
