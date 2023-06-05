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

    return xAxis, yAxis

############# Change setting here! #################
LAT50 = ["Latency Distribution", "50%"]
LAT75 = ["Latency Distribution", "75%"]
LAT90 = ["Latency Distribution", "90%"]
LAT99 = ["Latency Distribution", "99%"]
LATMAX = ["Latency", "Max"]
BARWIDTH = 32
####################################################

font = {'family' : 'normal',
        'weight' : 'normal',
        'size'   : 22}

plt.rc('font', **font)

Results = json.load(open("rd_results.json", "r"))
#Results = json.load(open("ed_results.json", "r"))

LatMaxX, LatMaxY = getAvgValues(Results, LATMAX)
Lat99X, Lat99Y = getAvgValues(Results, LAT99)
Lat90X, Lat90Y = getAvgValues(Results, LAT90)
Lat75X, Lat75Y = getAvgValues(Results, LAT75)
Lat50X, Lat50Y = getAvgValues(Results, LAT50)


plt.ylabel("Latency (ms)")
plt.xlabel("Connections (n)")
plt.xticks(LatMaxX)
plt.gca().set_ylim([0,1600])
plt.bar(LatMaxX, LatMaxY, label="MAX", width=BARWIDTH, color="#e6ecff", edgecolor="#000000")
plt.bar(Lat99X, Lat99Y, label="99th perc", width=BARWIDTH, color="#b3c4ff", edgecolor="#000000")
plt.bar(Lat90X, Lat90Y, label="90th perc", width=BARWIDTH, color="#668aff", edgecolor="#000000")
plt.bar(Lat75X, Lat75Y, label="75th perc", width=BARWIDTH, color="#003cff", edgecolor="#000000")
plt.bar(Lat50X, Lat50Y, label="50th perc", width=BARWIDTH, color="#001866", edgecolor="#000000")
plt.legend()
plt.show()