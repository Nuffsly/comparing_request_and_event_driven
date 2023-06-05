from matplotlib import pyplot as plt
import json

def getRawValues(obj, valuePath):
    xAxis = []
    yAxis = []
    for key, value in obj.items():
        connections = value["connections"]
        for key1, value1 in value.items():
            if(isinstance(value1, dict)):
                xAxis.append("C:{c} R:{r}".format(c = str(connections), r = str(key1)))
                runValue = value1
                for entry in valuePath:
                    runValue = runValue[entry]
                yAxis.append(runValue)

    plt.xlabel("Connections + Run")
    return xAxis, yAxis

def getAvgValues(obj, valuePath):
    xAxis = []
    yAxis = []
    for key, value in obj.items():
        xAxis.append(value["connections"])
        avgValue = 0
        runs = 0
        for key1, value1 in value.items():
            if(isinstance(value1, dict)):
                runs += 1
                runValue = value1
                for entry in valuePath:
                    runValue = runValue[entry]
                avgValue += runValue
        yAxis.append(avgValue / runs)

    
    plt.xticks(xAxis)
    return xAxis, yAxis

############# Change setting here! #################
VALUEPATH = ["Reqs/Sec"]
GETAVGVALUES = True
BARWIDTH = 16
####################################################

font = {'size'   : 22}

plt.rc('font', **font)

rdResults = json.load(open("rd_results.json", "r"))
edResults = json.load(open("ed_results.json", "r"))

if(GETAVGVALUES):
    rdXAxis, rdYAxis = getAvgValues(rdResults, VALUEPATH)
    edXAxis, edYAxis = getAvgValues(edResults, VALUEPATH)
else:
    rdXAxis, rdYAxis = getRawValues(rdResults, VALUEPATH)
    edXAxis, edYAxis = getRawValues(edResults, VALUEPATH)

plt.ylabel("Request per Second (n)")
plt.xlabel("Connections (n)")
plt.gca().set_ylim([0,4200])
plt.bar(rdXAxis, rdYAxis, label="Request-Driven", width=-BARWIDTH, align="edge")
plt.bar(edXAxis, edYAxis, label="Event-Driven", width=BARWIDTH, align="edge")
plt.legend()
plt.show()