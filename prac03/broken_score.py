
def main():
    score = float(input("Enter score: "))


def socre_judge(score):
    if score < 0 or score > 100:
        print("Invalid score")
    else:
        if score >= 90:
            print("Excellent")
        elif score >= 50:
            print("Passable")
        else:
            print("Bad")

main()