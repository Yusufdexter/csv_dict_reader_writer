from csv import DictReader, DictWriter

def cm_to_in(cm):
    return float(cm) * 0.393701

with open("fighter.csv") as file:
    csv_reader = DictReader(file)
    fighters = list(csv_reader)

with open("inches_fighters.csv", "w") as file:
    headers = ("Name", "State", "Height")
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for fight in fighters:
        csv_writer.writerow({
            "Name": fight["Name"],
            "State": fight["State"],
            "Height": cm_to_in(fight["Height (in cm)"])
    })