from client import CKYParser

def main():
    print("=== Testing CKY Probabilistic Grammar Parser ===")
    unary = {"time": [("N", 1.0)], "flies": [("V", 1.0)]}
    binary = {("N", "V"): [("S", 1.0)]}
    cky = CKYParser(unary, binary)
    prob = cky.parse(["time", "flies"])
    print("Parse probability:", prob)
    assert prob == 1.0
    print("=== All tests passed successfully! ===")

if __name__ == "__main__":
    main()
