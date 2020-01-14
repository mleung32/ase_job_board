import csv 

from ase_site.models import Posting

def convBool(value):
    if value == "TRUE":
        return True
    else: 
        return False

def run():
    with open('ASE_listings.csv') as f:
        reader = csv.reader(f)
        header = next(reader, None)

        Posting.objects.all().delete()

        for row in reader: 
            print(row)

            p, created = Posting.objects.get_or_create(
                classCode = row[0], 
                className = row[1],
                classDesc = row[2],
                semester = row[3],
                position = row[4],
                school = row[5],
                percentTime = row[6],
                hoursPerWk = row[7],
                feeRemission = convBool(row[8]),
                instructor = row[9],
                mode = row[10],
                instructorBio = row[11],
                classDays = row[12],
                classStartTime = row[13],
                classEndTime = row[14],
                sections = row[15],
                sectionLength = row[16],
                positionNotes = row[17],
                appDueDate = row[18],
                appURL = row[19]
            )
            p.save()