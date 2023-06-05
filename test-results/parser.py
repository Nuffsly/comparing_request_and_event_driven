import json
import re

def normaliseUnits(matches):
    normalMatches = []
    for match in matches:
        newMatch = match
        if(type(match) == tuple):
            match match[1]:
                case "s":
                    newMatch = float(match[0]) * 1000
                case "us":
                    newMatch = float(match[0]) / 1000
                case "k":
                    newMatch = float(match[0]) * 1000
                case "m":
                    newMatch = float(match[0]) * 60 * 1000
                case "KB":
                    newMatch = float(match[0]) / 1000
                case _:
                    newMatch = float(match[0])
        normalMatches.append(newMatch)
    return normalMatches

# Open files as tuples of source and target
files = []
EDTESTFILE = "ed_tests.txt"
RDTESTFILE = "rd_tests.txt"
files.append((open(EDTESTFILE, "r"), open("ed_results.json", "w")))
files.append((open(RDTESTFILE, "r"), open("rd_results.json", "w")))
decRegEx = r"(\d+.\d+)(\w+)?"

# Parse
for filePair in files:
    jsonObject = {}
    testFile = filePair[0].read()
    currTest = ""
    currRun = 0

    for line in testFile.split("\n"):
        # Wrk command line
        if(line.startswith("wrk")):
            currRun = 0
            matches = re.findall(r"[\-c|\-d](\d+)", line)
            matches = normaliseUnits(matches)
            currTest = "c:{c}".format(c=matches[0])
            jsonObject[currTest] = {"connections": int(matches[0])}
            continue
    
        # New run line
        if(line.startswith("Running")):
            currRun = int(currRun) + 1
            jsonObject[currTest][currRun] = {}
            continue

        # Latency line
        if(re.match(r" +Latency +[^\w]", line)):
            m = re.findall(decRegEx, line)
            m = normaliseUnits(m)
            jsonObject[currTest][currRun]["Latency"] = {"Avg":m[0], "Stdev":m[1], "Max":m[2], "Stdev +/-":m[3]} 
            continue
    
        # Req/Sec line
        if(re.match(r" +Req/Sec +", line)):
            m = re.findall(decRegEx, line)
            m = normaliseUnits(m)
            jsonObject[currTest][currRun]["Req/Sec"] = {"Avg":m[0], "Stdev":m[1], "Max":m[2], "Stdev +/-":m[3]} 
            continue

        # Latency Distribution
        if(re.match(r" +\d+%", line)):
            perc = re.match(r" +(\d+%)", line).group(1)
            m = re.findall(decRegEx, line)
            m = normaliseUnits(m)
            if("Latency Distribution" not in jsonObject[currTest][currRun].keys()):
                jsonObject[currTest][currRun]["Latency Distribution"] = {}
            jsonObject[currTest][currRun]["Latency Distribution"][perc] = m[0]
            continue

        # Totals line
        if(re.match(r" +\d+ requests", line)):
            m = re.findall(decRegEx, line)
            m = normaliseUnits(m)
            jsonObject[currTest][currRun]["Total reqs"] = m[0]
            jsonObject[currTest][currRun]["Total time"] = m[1]
            jsonObject[currTest][currRun]["Total data"] = m[2]
            continue

        # Reqs per second line
        if(line.startswith("Requests/sec")):
            m = re.findall(decRegEx, line)
            m = normaliseUnits(m)
            jsonObject[currTest][currRun]["Reqs/Sec"] = m[0]
            continue

        # Data per second line
        if(line.startswith("Transfer/sec")):
            m = re.findall(decRegEx, line)
            m = normaliseUnits(m)
            jsonObject[currTest][currRun]["Transferd/Sec"] = m[0]
            continue

    filePair[1].write(json.dumps(jsonObject))

# Close all files
for filePair in files:
    for textfile in filePair:
        textfile.close()