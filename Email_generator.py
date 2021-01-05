import numpy as np

fullNames = [['Mohamed Amine', 'Chadli'],
           ['Karim Sofiane', 'Chokri'],
           ['Khaled Mustapha', 'Sayed'],
           ['Fatima Aicha', 'Elkabir']]

def getRandomEmails(fullNamesList):
    domains = ['gmail', 'hotmail']
    emails = []
    for  fullName in fullNames:
        emails.append(f"{fullName[0].lower().replace(' ', '')}{fullName[1].lower().replace(' ', '')}{np.random.randint(0, 10)}{np.random.randint(0, 10)}{np.random.randint(0, 10)}@{np.random.choice(domains)}.com")
    return emails

getRandomEmails(fullNames)
