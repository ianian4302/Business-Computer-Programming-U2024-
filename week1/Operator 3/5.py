# Underweight BMI <18.5
# Normal range 18.5≤BMI<24
# Overweight 24≤BMI<27
# Mild obesity 27≤BMI<30
# Moderate obesity 30≤BMI<35
# Severe obesity 35≤35

BMI = float(input("Enter your BMI: "))
if BMI < 18.5:
    print("False, Underweight")
elif 18.5 <= BMI < 24:
    print("False, Normal range")
elif 24 <= BMI < 27:
    print("False, Overweight")
elif 27 <= BMI < 30:
    print("True, Mild obesity")
elif 30 <= BMI < 35:
    print("True, Moderate obesity")
else:
    print("True, Severe obesity")
