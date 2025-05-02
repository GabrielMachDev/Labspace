import pickle

with open('relatorio.pk1', 'rb') as archive:
    import_report = pickle.load(archive)

print(import_report)