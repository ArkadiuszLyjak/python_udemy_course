users = [
    {"name": "Arek", "email": "arek@wp.pl", "age": 20},
    {"name": "Ewa", "email": "ewa@wp.pl", "age": 25},
    {"name": "Kasia", "email": "kasia@wp.pl", "age": 30},
]


def return_lambda_filter_age_above(above_number):
    return lambda user: user["age"] > above_number


def return_lambda_multiply_by_x_age(multiplier):
    return lambda user: user["age"] * multiplier


def return_lambda_reduce_all_ages():
    return lambda user1, user2: user1["age"] + user2["age"]


list_of_users_above_25 = list(filter(return_lambda_filter_age_above(25), users))
print(list_of_users_above_25)
