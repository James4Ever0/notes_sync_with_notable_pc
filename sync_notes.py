import os
import subprocess
import time

sleepTime = 2

baseDir = "/root/Desktop/works/notes_ssh_keys"

targetGitDir = baseDir + "/notes"

logFile = baseDir + "/noteLog.log"

scriptPath = baseDir + "/sync_notes.sh"
checkNotableScript = baseDir + "/check_notable.sh"
fetchScript = baseDir + "/fetch_notes.sh"

commandList = ["ls", "--full-time","-lt",targetGitDir]

previousLog = None

def check_notable():
    mOutput = subprocess.check_output(["bash",checkNotableScript])
    mOutput = mOutput.decode("utf-8")
    processCount = int(mOutput.strip())
    return processCount

def execute_script(scriptPath):
    os.system("bash %s" % scriptPath)
# for whatever reason, execute the script once here.
print("INIT NOTES")

def fetch_script():
    execute_script(fetchScript)
import schedule

schedule.every(15).seconds.do(fetch_script)

while True:
    if check_notable() == 0:
        print("NOTABLE IS GONE")
        break
    if os.path.exists(logFile):
        with open(logFile,"r", encoding="utf-8") as f:
            previousLog = f.read()
    output = subprocess.check_output(commandList)
    output = output.decode("utf-8")

    if previousLog is not None:
        if previousLog != output: 
            print("HAVE CHANGES")
            print("UPLOADING NOTES")
            with open(logFile,"w+", encoding="utf-8") as f:
                f.write(output)
            execute_script(scriptPath)
    else:
        with open(logFile,"w+", encoding="utf-8") as f:
            f.write(output)
    # exit(0)
    schedule.run_pending()
    previousLog = output
    time.sleep(sleepTime)
