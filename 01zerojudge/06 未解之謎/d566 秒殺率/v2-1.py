from sys import stdin


def grouper(arr: list, wid: int = 2):
    iterators = [iter(arr)] * wid
    return zip(*iterators)


def main():
    _, *ipt = stdin.read().split()
    ipt.reverse()
    record = dict()
    total_ac = total_ac_instantly = 0
    for score, name in grouper(ipt):
        if name in record:
            total_ac += not record[name] and score == "AC"
            record[name] = record[name] or score == "AC"
        else:
            record[name] = score == "AC"
            if score == "AC":
                total_ac += 1
                total_ac_instantly += 1
    print(f"{total_ac_instantly / total_ac:.0%}")


main()
