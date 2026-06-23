
from inspection import Inspection
from scorer import Scorer
from reporter import Reporter
scorer = Scorer()
reporter = Reporter()

while True:
    print("\n---Welcome to the Password Strength Checker.---\n")
    user_password = input("Let me know the password that you want to analyze.\n")

    inspector = Inspection(user_password)
    raw_facts = inspector.analyze()
    score, feedback = scorer.calculate_score(raw_facts)
    reporter.report(score)
    reporter.advise(feedback)

    user_choice = input("\nDo you want to check strength for another password? Type (Y/N)\n").lower()
    if user_choice != "y":
        print("Thanks for using the Password Strength Checker.")
        break