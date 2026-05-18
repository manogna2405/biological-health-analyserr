# Parent Class
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


# Child Class
class HealthAnalyzer(Person):
    def __init__(self, name, age, weight, height, heart_rate, glucose):
        super().__init__(name, age)
        self.weight = weight
        self.height = height
        self.heart_rate = heart_rate
        self.glucose = glucose

    def calculate_bmi(self):
        return self.weight / (self.height ** 2)

    def analyze_health(self):
        bmi = self.calculate_bmi()

        report = {
            "Name": self.name,
            "Age": self.age,
            "BMI": round(bmi, 2)
        }

        # BMI Status
        if bmi < 18.5:
            bmi_status = "Underweight"
        elif bmi < 25:
            bmi_status = "Normal"
        elif bmi < 30:
            bmi_status = "Overweight"
        else:
            bmi_status = "Obese"

        # Heart Rate Status
        heart_status = "Normal" if 60 <= self.heart_rate <= 100 else "Abnormal"

        # Glucose Status
        glucose_status = "Normal" if self.glucose < 140 else "High"

        # Overall Health
        if bmi_status == "Normal" and heart_status == "Normal" and glucose_status == "Normal":
            overall = "Healthy"
        else:
            overall = "Unhealthy"

        report["BMI Status"] = bmi_status
        report["Heart Rate Status"] = heart_status
        report["Glucose Status"] = glucose_status
        report["Overall Health"] = overall

        return report


# Input without printing prompts
try:
    name = input()
    age = int(input())
    weight = float(input())
    height = float(input())
    heart_rate = int(input())
    glucose = int(input())

    person = HealthAnalyzer(name, age, weight, height, heart_rate, glucose)
    result = person.analyze_health()

    print("\n--- Health Report ---")
    for key, value in result.items():
        print(key, ":", value)

except ValueError:
    print("Invalid input! Please enter correct data type.")