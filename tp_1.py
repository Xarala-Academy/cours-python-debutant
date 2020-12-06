from statistics import mean
transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]

# ordonner = sorted(transaction_list)
# print(transaction_list)
# transaction_list.sort()
# print(transaction_list)
# transaction_list.sort(reverse=True)
# print(transaction_list)

# transaction_uniques = []
# for transaction in transaction_list:
#     if transaction not in transaction_uniques:
#         transaction_uniques.append(transaction)

# print(transaction_uniques)


# transaction_listes = deepcopy(transaction_list)
# transaction_list = [568]
# transaction_listes[0] = 678
# print("D", transaction_listes, transaction_list)
print(sum(transaction_list) / len(transaction_list))
print(mean(transaction_list))
