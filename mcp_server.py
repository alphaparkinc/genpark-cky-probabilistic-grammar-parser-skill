import sys
import json
from client import CKYParser

def main():
    while True:
        line = sys.stdin.readline()
        if not line:
            break
        req = json.loads(line)
        method = req.get("method")
        params = req.get("params", {})
        if method == "parse":
            unary = params.get("unary", {})
            raw_bin = params.get("binary", {})
            bin_rules = {tuple(k.split(",")): v for k, v in raw_bin.items()}
            parser = CKYParser(unary, bin_rules)
            p = parser.parse(params.get("words", []))
            res = {"probability": p}
        else:
            res = {"error": "unknown method"}
        sys.stdout.write(json.dumps({"id": req.get("id"), "result": res}) + "\n")
        sys.stdout.flush()

if __name__ == "__main__":
    main()
