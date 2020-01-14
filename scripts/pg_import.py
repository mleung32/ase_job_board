import psycopg2
import csv

def run():
    conn = psycopg2.connect("host=localhost dbname=ase_db user=ase_owner")
    cur = conn.cursor()

    with open("ASE_part2.csv", "r") as f:
        cur.copy_from(f, "ase_site_posting", sep=",", columns=('"classCode"', '"className"', '"classDesc"',
        "semester", "position", "school", '"percentTime"', '"hoursPerWk"', '"feeRemission"', "instructor","mode", 
        '"instructorBio"', '"classDays"', '"classStartTime"', '"classEndTime"', '"numPositions"',
        '"positionNotes"', '"appDueDate"', '"appURL"'))

        conn.commit()
        conn.close()