import csv

def loe_csv_fail(nimi):
    tabel = []
    with open(nimi, encoding="utf-8") as fail:
        csv_fail = csv.reader(fail, delimiter=";")
        for rida in csv_fail:
            tabel.append(rida)
    return tabel