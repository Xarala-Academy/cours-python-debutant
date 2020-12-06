transaction_list = [250, 12, 45, 32, 23, 25, 250, 12]

# Tache 1 : Ecrire un programme qui fait la somme des transactions.
print(sum(transaction_list))
somme_des_transactions = 0
for transaction in transaction_list:
    somme_des_transactions += transaction

print(somme_des_transactions)

# Tache 2 : Afficher la 5eme transaction
print(transaction_list[5])

# Tache 3 : Boucler la liste et afficher les éléments un a un
for transaction in transaction_list:
    print("Transaction : ", transaction)

# Tache 4 : Ordonner la liste
ordonner = sorted(transaction_list)
print(ordonner)
# Tache 5 : Afficher la transaction la plus petite
transaction_plus_petite = min(transaction_list)
print(transaction_plus_petite)
# Tache 6 : Afficher la dernière transaction
print(transaction_list[-1])
# Tache 7 : Supprimer les transactions dupliquées
transaction_list = list(set(transaction_list))
print(transaction_list)
# Tache 8 : Supprimer la dernière transaction
del transaction_list[-1]
print(transaction_list)
# Tache 9 : Créer une copie des transactions
transaction_listes = []
transaction_listes = transaction_list[:]
print(transaction_listes)
# Tache 10 : Ecrire un programme qui fais la moyenne des transactions

print(sum(transaction_list) / len(transaction_list))
# Tache 11 : Convertir la liste en tuple
transaction_tuples = tuple(transaction_list)
print(transaction_tuples)
