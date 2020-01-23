def do(): #the main function. up here to be easier to see, hide other functions
  newData = getNewDataFromUser()
  writeDataToFile(newData) #save the new Data to bottom of file

  data = loadData() #get all data, new and old (adds extra read, but more secure)

  times = convertDataToInt(data) #put data into number form from string


  totalSeconds = sum(times) #add it all up to show total
  output = convertSecondsToMinutes(totalSeconds)
  print(output)

def loadData():
  f = open("times.txt", "r") #read file
  if f.mode == "r":
    data = f.read().splitlines()
    print("Data Loaded")
    f.close()
    return data

def writeDataToFile(inData):
  f = open("times.txt", "a") 
  for listitem in inData:
    f.write('%s\n' % listitem)

def convertDataToInt(temp):
  times = [float(x) for x in temp] #take from string to float
  times = [int(x) for x in times] #take from float to int
  return times

def getNewDataFromUser():
  flag = 0
  data = []
  while flag == 0:
    num = eval(input("Gimme a time m.s or 0 to add it all up: "))
    if num == 0:
      flag = 1
    else:
      data.append(num)
  data = convertToSeconds(data)
  return data

def convertToSeconds(inData):
  i = 0
  for x in inData:
    minutes = inData[i] // 1
    seconds = inData[i] % 1
    time = (int(minutes) * 60) + int(seconds * 100)
    inData[i] = time
    i += 1
  return inData

def convertSecondsToMinutes(time):
  x = str(int(time//60))
  y = str(int(time % 60))
  length = x + " minutes and " + y + " seconds"
  return length



do() #actually run the thing