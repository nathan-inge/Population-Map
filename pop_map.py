def createCityPopDict():
    file = open('pop3.txt','r')
    s = file.read()
    file.close()
    D ={}

    lines = s.split('\n')    

    for eachLine in range(len(lines)-1):
        cityPop = lines[eachLine].split()

        strPop = ''.join(cityPop[-1:])
        intPop = int(strPop)        
            
        D[' '.join(cityPop[1:-1])] = intPop

    return D

def createCityLatLonDict():
    file=open('latlon3.txt','r')
    s=file.read()
    file.close()
    lines=s.split('\n')
    D={}
    for i in range(len(lines)-1):
        city=lines[i].split()
        val=(float(city[0]),-float(city[1]))
        cityName=' '.join(city[2:])
        D[cityName]=val
    return D
def createStateColorDict():
    file=open('stateAdj.txt','r')
    s=file.read()
    file.close()
    lines=s.split('\n')
    D={}
    states=lines[:-1:2]
    num=lines[1::2]
    i=0
    for mutiStates in states:
        eachState=mutiStates.split(',')
        state = eachState[0]
        state=state.lower()
        D[state]=int(num[i])
        i+=1
    return D

import cTurtle
import math
def drawLower48Map():
    cityPopDict = createCityPopDict()
    cityLatLonDict = createCityLatLonDict()
    stateColorDict = createStateColorDict()
    colorList = ['red','green','blue','purple']
    listLat = []
    listLon = []

    cities = cityLatLonDict.keys()

    for city in cities:
        latLon = cityLatLonDict[city]
        listLat.append(latLon[0])
        listLon.append(latLon[1])    

    minLat = min(listLat)
    maxLat = max(listLat)
    minLon = min(listLon)
    maxLon = max(listLon)

    t = cTurtle.Turtle('turtle')
    t.ht()
    t.setWorldCoordinates(minLon,minLat,maxLon,maxLat)

    outputText = ''
    outputText += '{0:30}{1:15}{2:15}{3:15}{4:15}{5:15}\n'.format('cityname:','latitude:','longitude:','population:','dot size:','dot color:')
    outputText += '\n'
    

    for city in cities:
        latLon = cityLatLonDict[city]
        x = latLon[1]
        y = latLon[0]

        l = city.split(',')
        state = ''.join(l[-1:])
        colorIndex = stateColorDict[state]
        color = colorList[colorIndex]

        #print(city,' (',x,',',y,')')

        if city in cityPopDict:
            dotSize = 4 + math.ceil(math.sqrt(cityPopDict[city]/50000))
            pop = cityPopDict[city]
        else:
            dotSize = 4
            pop = '-'

        t.up()
        t.setposition(x,y)
        t.down()
        t.dot(dotSize,color)

        outputText += '{0:30}{1:<15}{2:<15}{3:<15}{4:<15}{5:15}\n'.format(city,y,(x*-1),pop,dotSize,color)

    file = open('output.txt','w')
    file.write(outputText)
    file.close()


drawLower48Map()

    
        

    

   

    
    
    
        
    


    

        
        
                    
