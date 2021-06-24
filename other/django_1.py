# Fizz Buzz!
#
# def fizz_buzz():
#     x = int(input("Input an integer: "))
#     for i in range(1, x+1):
#         if i % 15 == 0:
#             print('fizz-buzz')
#         elif i % 5 == 0:
#             print('buzz')
#         elif i % 3 == 0:
#             print('fizz')
#         else:
#             print(i)
#
#
# fizz_buzz()

# items = [
#     ('apple', 15),
#     ('grape', 45),
#     ('orange', 25),
#     ('potato', 7),
# ]
#
# # filter_obj = filter(lambda item: item[1] >= 10, items)
# #
# # print((next(filter_obj))[0])
# # print((next(filter_obj))[0])
# # print((next(filter_obj))[0])
#
#
# filtered = list(filter(lambda item: item[1] >= 10, items))
#
# for i in filtered:
#     print(i[0])



items = [
    ('apple', 15),
    ('grape', 45),
    ('orange', 25),
    ('potato', 7),
    ('onion', 7),
]

# price = []
# for i in items:
#     price.append(i[1])


prices = map(lambda item: item[1], items)
print(list(prices))
