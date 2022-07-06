import os
import json

dbControlFolders = [folder.upper() for folder in os.listdir(os.path.abspath("control")) if os.path.isdir(os.path.join(os.path.abspath("control"),folder))]
print("List of databases applieds:")
for database in dbControlFolders:
    print("- " + database)

def printTableInfo(infos):
    if not len(infos):
        print("No informations.")
    else:
        len_of_fields = []
        len_general = [len(length) for length in infos[0]]
        result = []

        for field in infos:
            len_of_fields.append([len(length) for length in field])
            for idx in range(0,len(field)):
                len_general[idx] = len(field[idx]) if len(field[idx]) > len_general[idx] else len_general[idx]

        for info in infos:
            line = []
            for idx in range(0,len(info)):
                n = (len_general[idx]) - len(info[idx])
                line.append(info[idx] + "".join([c*n for c in " "]))

            result.append(line)
                
        for line in result:
            printer = ""
            for idx in range(0,len(line)):
                printer += line[idx] + " | "
            print(printer)

def listDetailsDb(database):
    versions_database = json.loads(open(os.path.abspath("control/"+database+"/versions_applied.json"),"r").read())
    infos = [("Database","Version","File","Last_Date_Execution","Status","Description")]
    for version in versions_database:
        infos.append((version["database"], version["version"], version["file"],version["last_date_execution"],version["status"],version["description"]))

    printTableInfo(infos)

if len(dbControlFolders):
    dbNameChoiced = str(input("Choose a database to more details. Please inform the databases name to side or write 'bye' to exit program: ")).upper()
    if dbNameChoiced not in dbControlFolders:
        print("See you later. Bye!")
    else:
        listDetailsDb(dbNameChoiced)