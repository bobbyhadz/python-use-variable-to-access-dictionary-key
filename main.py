# Using a variable to access a dictionary Key in Python

# 👇️ keys are strings
my_dict = {
    '1': 'bobby',
    '2': 'hadz'
}

# 👇️ variable is an integer
variable = 1

print(my_dict[str(variable)])  # 👉️ bobby