li1=[10,20,30,40,50,"Babu",True,False]# list is a data struture and also it is munable : it can change value at the time of operation,it is indexed and ordered
l=[55,60,70,85,95,55,10,100,50]
li2=[2,5,6,7,8,9,0,"Haimi"]
print("==============Printing Data type===========")
print(type(li1))#Retrive data type and Data structure#
 

print("========Printing Whole Lists==========")
print(li1)
print(l)
print(li2)

print("==============Printing Asper index===========")

print(li1[3])#Retrive value given index
print("==============Printing Length of the list===========")
print(len(li1)) #Retrive Length of List

print("==============Inserting new value===========")

li1.insert(5,"Ewan")#Insert new value with replace existing value.
print(li1)
print("============== Appending Data===========")
li1.append("Hameed")
print(li1)
print("==============Adding two list===========")
li1.extend(li2)
print(li1)
print("==============Slicing values===========")

print(li1[0:5])

print(li1[:5])

print(li1[2:])
print("=======Reverse slicing======")

print(li1[-4])
print(li1[-5:-2])
print("==============Removing a value===========")
li1.remove("Babu")
print(li1)

print("==============Sorting Data===========")
l.sort()
print(l)
print("==============Printin Descending order===========")
print(l)
l.reverse()
print(l)
print("======Printing list before pop=======")
print(li1)
print("=====Printing after pop======")
li1.pop()
print(li1)
print("====pop an element asper index======")
li1.pop(5)
print(li1)












