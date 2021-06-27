x = [0, 1, 2, 3]

print(all([y > 0 for y in x]))
print(any([y > 0 for y in x]))

def unlimited_arguments(*args):
    print(args)
    for argument in args:
        print(argument, end= "")

unlimited_arguments(1,2,3,4,5)
unlimited_arguments(*[1,2,3,4,5])

def unlimited_arguments_for_dictionaries(**kwargs):
    print(kwargs)
    for k, argument in kwargs.items():
        print(k, argument, end= "")

unlimited_arguments_for_dictionaries(name="sanyi",cisk = "eszti")