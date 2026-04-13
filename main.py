def calculate_bmi(weight, height):
    return weight / (height * height)

def get_score(bmi, sleep, hbp, lbp, sm, cig, drink, age):
    score = 0
    reasons = []
    suggestions = []

    if bmi < 18.5:
        score += 1
        reasons.append("Low BMI")
        suggestions.append("Increase healthy calorie intake")
    elif bmi > 25:
        score += 1
        reasons.append("High BMI")
        suggestions.append("Exercise regularly and manage diet")

    if sleep < 6:
        score += 1
        reasons.append("Low sleep")
        suggestions.append("Try to sleep at least 7–8 hours daily")
    elif sleep > 9:
        score += 1
        reasons.append("Oversleeping")
        suggestions.append("Maintain a consistent sleep schedule")

    if hbp == "y":
        score += 1
        reasons.append("High BP")
        suggestions.append("Reduce salt intake and manage stress")

    if lbp == "y":
        score += 1
        reasons.append("Low BP")
        suggestions.append("Stay hydrated and consult a doctor if needed")

    if sm == "y":
        score += 2
        reasons.append("Smoking")
        suggestions.append("Try to reduce or quit smoking")
        if cig > 5:
            score += 1
            reasons.append("Heavy smoking")
            suggestions.append("Seek help to reduce cigarette consumption")

    if drink == "y":
        score += 1
        reasons.append("Alcohol consumption")
        suggestions.append("Limit alcohol intake")

    if age > 45:
        score += 1
        reasons.append("Age risk factor")
        suggestions.append("Regular health checkups recommended")

    return score, reasons, suggestions


print("❤️ WELCOME TO HEART HEALTH CHECK ❤️")

while True:
    print("\n--- NEW USER ---")

    age = int(input("Enter your age: "))
    weight = float(input("Enter your weight (kg): "))
    height = float(input("Enter your height (m): "))
    sleep = int(input("Hours of sleep per day: "))

    hbp = input("High BP? (y/n): ")
    lbp = input("Low BP? (y/n): ")
    sm = input("Do you smoke? (y/n): ")
    drink = input("Do you drink? (y/n): ")

    cig = 0
    if sm == "y":
        cig = int(input("Cigarettes per day: "))

    bmi = calculate_bmi(weight, height)
    score, reasons, suggestions = get_score(bmi, sleep, hbp, lbp, sm, cig, drink, age)

    print("\n--- RESULT ---")
    print("Your BMI is:", round(bmi, 2))

    if score <= 2:
        print("Heart Health: GOOD ❤️")
    elif score <= 5:
        print("Heart Health: MODERATE ⚠️")
    else:
        print("Heart Health: POOR ❌")

    print("\nReasons affecting your health:")
    for r in reasons:
        print("-", r)

    print("\nRecommendations for you:")
    for s in suggestions:
        print("✔", s)

    choice = input("\nDo you want to check another user? (y/n): ")
    if choice.lower() != "y":
        print("👋 Thank you for using Heart Health Check!")
        break
