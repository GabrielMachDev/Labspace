import pickle

report = {
    'Client': 'Gabriel Mach',
    'total': 3570.89,
    'products': ['iphone', 'airpod', 'applewatch'],
    'paid': True
}

with open('relatorio.pk1', 'wr') as archive:
    pickle.dump(report, archive)