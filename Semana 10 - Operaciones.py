import random

# Crear un conjunto ficticio de 500 usuarios
total_users = set(f'User_{i}' for i in range(1, 501))

# Crear conjuntos ficticios para usuarios vacunados
pfizer_users = set(f'User_{i}' for i in random.sample(total_users, 75))
astra_users = set(f'User_{i}' for i in random.sample(total_users, 75))

# Asegurarse de que hay usuarios en ambos conjuntos de vacunas
# Esto asegura que hay usuarios que tienen ambas vacunas
common_users = pfizer_users & astra_users
if len(common_users) < 10:
    additional_users = set(random.sample(total_users - pfizer_users - astra_users, 10 - len(common_users)))
    pfizer_users.update(additional_users)
    astra_users.update(additional_users)

# Operaciones de conjuntos
not_vaccinated = total_users - (pfizer_users | astra_users)
both_vaccines = pfizer_users & astra_users
only_pfizer = pfizer_users - astra_users
only_astra = astra_users - pfizer_users

# Imprimir resultados
print("Listado de ciudadanos que no se han vacunado:")
print(not_vaccinated)
print("\nListado de ciudadanos que han recibido las dos vacunas:")
print(both_vaccines)
print("\nListado de ciudadanos que solamente han recibido la vacuna de Pfizer:")
print(only_pfizer)
print("\nListado de ciudadanos que solamente han recibido la vacuna de AstraZeneca:")
print(only_astra)
