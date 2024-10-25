# Tax Calculator Based on Gross Income
def task9():
    gross_income = float(input("Enter your gross income in £: "))
    
    if gross_income <= 12500:
        tax_owed = 0
    elif gross_income <= 50000:
        tax_owed = (gross_income - 12500) * 0.20
    elif gross_income <= 150000:
        tax_owed = (37500 * 0.20) + (gross_income - 50000) * 0.40
    else:
        tax_owed = (37500 * 0.20) + (100000 * 0.40) + (gross_income - 150000) * 0.45

    net_income = gross_income - tax_owed
    
    print(f"Tax Owed: £{tax_owed:.2f}")
    print(f"Net Income after Tax: £{net_income:.2f}")
    
#Task: Advanced Grade Calculation System
# Get user input and validate it is within the range 0-100
def task10():
    def get_score(score_type):
        score = float(input(f"Enter your {score_type} score (0-100): "))
        while score < 0 or score > 100:
            print("Score must be between 0 and 100.")
            score = float(input(f"Enter your {score_type} score (0-100): "))
        return score

    coursework = get_score("coursework")
    midterm = get_score("midterm")
    final_exam = get_score("final exam")

    final_score = coursework * 0.40 + midterm * 0.25 + final_exam * 0.35

    if final_score >= 70:
        letter_grade = "A"
    elif final_score >= 50:
        letter_grade = "B"
    elif final_score >= 40:
        letter_grade = "C"
    else:
        letter_grade = "F"

    # Display results
    print(f"Final score: {final_score:.2f}")
    print(f"Letter grade: {letter_grade}")
