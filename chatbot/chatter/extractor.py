import csv

def extract():
    with open('./chatter/cigarette-db.csv', newline='') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
        i = 0;
        conversation = []
        for row in spamreader:
            if not i == 0:
                #print(', '.join(row))
                conversation.append(row[3])
                conversation.append(row[6])
            i = i + 1

    return conversation





