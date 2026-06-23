from scorer import Scorer
class Reporter:

    def __init__(self):
        pass


    def report(self, score):
        if score >= 8:
            print(f"your password is strong. with score: {score}/10")

        elif score >= 6:
            print(f"your password is medium. with score: {score}/10")

        elif score < 6:
            print(f"your password is weaker. with score: {score}/10")

    def advise(self, feedback):
        if feedback == []:
            print("Excellent! Your password meets all security guidelines.")

        else:
            print("you need to work on below points to make your password secure.")
            for index, feedback in enumerate(feedback,start=1):
                print(f"{index}. {feedback}")

