import pyodbc
import os
import json
from datetime import datetime
from pathlib import Path

# Functions
def formatDateTime_nameFile():
    return str(datetime.now()).replace(" ","_").replace("-","").replace(":","").replace(".","")[:15]

def generateJsonStructure(arrayFiles,reverse):
    if not len(arrayFiles):
        return []

    db_versions = []
    versions_todo_json = []
    idFile = 1
    arrayFiles.append(("","",""))

    for (file, version, database) in arrayFiles:
        db_temp = database if idFile == 1 else db_temp
        idFile += 1

        if db_temp != database:
            db_versions.append({"database":db_temp, "versions":sorted(versions_todo_json,key=lambda doc:int(doc["version"]), reverse=reverse)})
            versions_todo_json = []
            db_temp = database

        versions_todo_json.append({"version":version, "file": file})
    
    return db_versions

def applyScriptDb(path, file, log, tag_description):
    description = ""
    infos_processes = []
    executed = True
    log_content = []
    script = open(os.path.abspath(f"{path}/{file}"),"r").read()
    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Executing file... --> " + file)
    print("Executing file... --> " + file)

    for stmt in script.split(";"):
        if stmt != "":
            if len(tag_description) <= len(stmt):
                if tag_description.lower() == stmt[:len(tag_description)].lower():
                    description = stmt.replace(tag_description,"").strip()
                    continue
            try:
                with (connection.cursor()) as cursor:
                    cursor.execute(f"{stmt};")
                    connection.commit()
                    if len(cursor.messages):
                        for (code, message) in cursor.messages:
                            log_content.append(f"{str(datetime.now())} - code:{code}, message:{message}, file:{file}, status:success \n")
            except pyodbc.Error as ex:
                log_content.append(f"{str(datetime.now())} - code:{ex.args[0]}, message:{ex.args[1]}, file:{file}, status:failed \n")
                executed = False
    
    archive = open(os.path.abspath(log_file.replace("[file]",log)),"w")
    for line in log_content:
        archive.write(str(line))
    
    archive.close()
    return (executed, infos_processes, description)

# Variables
dbmaster_datasource = "DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-SCVFDSG\SQL2019A;DATABASE=master;UID=dbapply;PWD=dbapply;autocommit=True"
connection = pyodbc.connect(dbmaster_datasource)
connection.autocommit = True

todo = sorted([(file, file.split("_")[0].replace("v",""), file[len(str(file.split("_")[0].replace("v",""))) + 2:-4]) for file in os.listdir(os.path.abspath("todo")) if file[-4:] == ".sql"], key=lambda tup:tup[2])
rollback = sorted([(file, file.split("_")[0].replace("v",""), file[len(str(file.split("_")[0].replace("v",""))) + 2:-4]) for file in os.listdir(os.path.abspath("rollback")) if file[-4:] == ".sql"], key=lambda tup:tup[2])

log_file = "log/[file]_" + formatDateTime_nameFile() + ".log"

todo = generateJsonStructure(todo,False)
rollback = generateJsonStructure(rollback,True)

print("***** Started execution db_pipeline. *****")

if len(rollback):
    infos_processes = []
    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Executing [rollback] folder.\n")
    print("Executing [rollback] folder.")

    for folder in rollback:
        folder_done_rollback = os.path.abspath("done/" + folder["database"] + "/rollback")
        folder_control_version = os.path.abspath("control/" + folder["database"])
        versions_json = json.loads(open(os.path.abspath("control/" + folder["database"] + "/versions_applied.json"), "r").read()) if os.path.exists(os.path.abspath("control/" + folder["database"] + "/versions_applied.json")) else []

        if versions_json == []:
            infos_processes.append("[" + formatDateTime_nameFile() + "] :: Not exists versions applied... --> control/" + folder["database"] + "/versions_applied.json \n")
            print("Not exists versions applied... --> control/" + folder["database"] + "/versions_applied.json")
            continue

        Path(folder_done_rollback).mkdir(parents=True, exist_ok=True)

        for version in folder["versions"]:
            if version["version"] in [versions["version"] for versions in versions_json]:
                log_name_file = "Rollback_" + version["file"].replace(".sql","")
                (executed, infos, description) = applyScriptDb(file=version["file"], path="rollback", log=log_name_file, tag_description="--##Commit")
                infos_processes += [info + "\n" for info in infos]
                if executed:
                    versions_json.pop(versions_json.index(next(idx for idx in versions_json if idx["version"]==version["version"])))
                    print("Erase version from versions file... --> " + ( folder_control_version + "/versions_applied.json"))
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Erase version from versions file... --> " + folder_control_version + "/versions_applied.json \n")
                    os.rename(os.path.abspath("rollback/" + version["file"]),os.path.abspath("done/" + folder["database"] + "/rollback/" + version["file"]))
                    print("Moving file to done/rollback... --> " + folder_done_rollback + "/" + version["file"])
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Moving file to done/rollback... --> " + folder_done_rollback + "/" + version["file"] + "\n")
                else:
                    print("Not move file to done... see more details in log file. ("+ log_name_file +")")
                    print("This processes was aborted.")
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Not move file to done... see more details in log file. ("+ log_name_file +") \n")
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: This processes was aborted. \n")
                    break

        versions_json = sorted(json.loads(json.dumps(versions_json, indent=4, ensure_ascii=False)), key=lambda doc:doc["last_date_execution"], reverse=True)
        with open(os.path.join(folder_control_version, "versions_applied.json"),"w") as versionsFile:
            versionsFile.write(json.dumps(versions_json, indent=4, ensure_ascii=False))
            versionsFile.close()

        with open(os.path.join(folder_control_version,"debug.log"),"a") as debugFile:
            debugFile.writelines(infos_processes)
            debugFile.close()

if len(todo):
    print("Executing [todo] folder.")
    infos_processes = ["[" + formatDateTime_nameFile() + "] :: Executing [todo] folder.\n"]

    for folder in todo:
        folder_control_version = os.path.abspath("control/" + folder["database"])
        folder_done = os.path.abspath("done/" + folder["database"])

        Path(folder_control_version).mkdir(parents=True, exist_ok=True)
        Path(folder_done).mkdir(parents=True, exist_ok=True)
    
        versions_json = json.loads(open(os.path.abspath("control/" + folder["database"] + "/versions_applied.json"), "r").read()) if os.path.exists(os.path.abspath("control/" + folder["database"] + "/versions_applied.json")) else []
        for version in folder["versions"]:
            if version["version"] not in [versions["version"] for versions in versions_json]:
                log_name_file = "ToDo_" + version["file"].replace(".sql","")
                (executed, infos, description) = applyScriptDb(file=version["file"], path="todo", log=log_name_file, tag_description="--##Commit")
                infos_processes += [info + "\n" for info in infos]
                versions_json.append({
                        "database": folder["database"],
                        "version": version["version"],
                        "file": version["file"],
                        "last_date_execution": str(datetime.now()),
                        "status":("executed" if executed else "not executed"),
                        "description": description
                    })

                if executed:
                    os.rename(os.path.abspath("todo/" + version["file"]), os.path.join(folder_done,version["file"]))
                    print("Moving file to done... -> " + folder["database"] + "/" + version["file"])
                    print("Updated version file... -> control/" + folder["database"] + "/versions_applied.json")
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Moving file to done... -> " + folder["database"] + "/" + version["file"] + "\n")
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Updated version file... -> control/" + folder["database"] + "/versions_applied.json \n")
                else:
                    print("Not move file to done... see more details in log file. ("+ log_name_file +")")
                    print("This processes was aborted.")
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: Not move file to done... see more details in log file. ("+ log_name_file +") \n")
                    infos_processes.append("[" + formatDateTime_nameFile() + "] :: This processes was aborted. \n")
                    break

        versions_json = sorted(json.loads(json.dumps(versions_json, indent=4, ensure_ascii=False)), key=lambda doc:doc["last_date_execution"], reverse=True)
        with open(os.path.join(folder_control_version, "versions_applied.json"),"w") as versionsFile:
            versionsFile.write(json.dumps(versions_json, indent=4, ensure_ascii=False))
            versionsFile.close()

        with open(os.path.join(folder_control_version,"debug.log"),"a") as debugFile:
            debugFile.writelines(infos_processes)
            debugFile.close()


print("***** Finished execution db_pipeline. *****")