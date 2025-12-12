#While statement/ loop
samplelist = [1,2,3,12,5,6,8]
length = len(samplelist)
count = 0

while length > 0:
  samplelist[count] = samplelist[count] = 2
  count= count + 1
  length = length - 1




print(samplelist)
#print (count)
#print(length)



#For statement /Loop
samplelist = [1,2,3,12,5,6,8]
for i in samplelist:
  i = i + 2
  print(samplelist)
  print(f"i (i)")




#For statement /Loop
samplelist = [1,2,3,12,5,6,8]
for index, value in enumerate(samplelist):
    samplelist[index] = samplelist[index] + 2
    print(samplelist)


#For statement /Loop
samplelist = [1,2,3,12,5,6,8]
for index in range(len(samplelist)):
    samplelist[index] = samplelist[index] + 2
    print(samplelist)




#If Statement / Loop ==> terms: if,elif,else

laptopRAM = 4
fawazram = 3
if fawazram >= laptopRAM:
   print('welcome my fawaz')
elif fawazram >=3:
   print('Enter the class but make sure you upgrade your RAM')
else:
   print('Yours is not enough to take the course,you need to go')



   flightCost = 12000000

   firstclass = 100000000
   secondclass =300000
   thirdclass = 600000

   if flightCost >= firstclass:
        print('You can enter first,second or third class')
   elif flightCost >= secondclass:
       print ('You can enter second or third')
   elif flightCost >=thirdclass:
        print('You can enter third class only')
   else :
        print('Insufficient balance')


#assignment hint
a = 4
if 0 < a <=5:
    print ('a is between 0 and 5')

a = 15
if 16 > a >=20:
    print('a is less than  16')
else:('everthing is equal')