import psycopg2

def run():
    conn = psycopg2.connect("host=localhost dbname=ase_db user=ase_owner")
    cur = conn.cursor()
    cur.execute(
        """CREATE TABLE ase_site_posting(
        postingID       SERIAL PRIMARY KEY,
        classCode       TEXT,    
        className       TEXT, 
        classDesc       TEXT, 
        semester        TEXT,
        position        TEXT, 
        school          TEXT,
        percentTime     INTEGER, 
        hoursPerWk      INTEGER,
        feeRemission    BOOLEAN, 
        instructor      TEXT, 
        mode            TEXT, 
        instructorBio   TEXT, 
        classDays       TEXT,
        classStartTime  TIME, 
        classEndTime    TIME, 
        numPositions    INTEGER,
        positionNotes   TEXT, 
        appDueDate      TEXT,
        appURL          TEXT)
    """)

    conn.commit()
    conn.close()