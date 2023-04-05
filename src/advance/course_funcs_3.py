def goodie(csv):
    with open(csv, "r") as f:
        txt = f.read()
        f.close()
    lines = txt.splitlines()
    lines = [l.replace(",good,", "") for l in lines if "good" in l]
    return lines