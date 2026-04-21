# Un lecteur v1 (qui ne connaît pas "classification")
# ignore simplement le champ 5 — pas d'erreur.
# Les champs inconnus sont préservés dans le buffer
# → rétrocompatibilité native de Protobuf.

# Simulons : on lit binary_data (v2) avec le même proto
# mais en n'accédant qu'aux champs v1 :
print(f"ID: {doc2.id}, Title: {doc2.title}, Author: {doc2.author}")
# Fonctionne parfaitement — les champs v2 sont simplement ignorés
