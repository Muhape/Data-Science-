def main():
    name = input("What is your name?")
    weight = float(input("Tell me your weight in kg: "))
    height = float(input("Tell me your height in meters: "))
    bmi = float(weight / (height ** 2))
    calc_bmi = round(bmi, 2)
    print(f"Hello {name} Your BMI is {calc_bmi}")
    bmi_result(calc_bmi)

def bmi_result(n):
    if n < 18.5:
        print("You are an Underweight")
    elif n < 24.9:
        print("You are a Normal Weight")
    elif n < 30:
        print("You are an Overweight")
    else:
        print("You are an Obese")
main()