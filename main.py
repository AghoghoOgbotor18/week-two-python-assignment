my_list = []
my_list.append(10) #append first element since append append can't take more than argument
my_list.append(20) #append second element
my_list.append(30) #append third element
my_list.append(40) #append fourth element
print(my_list) #[10,20,30,40]
my_list[1] = 15 #insert the value 15 at the second position
print(my_list) #[10,15,30,40]
sec_list =[50, 60, 70] #a new list
my_list.extend(sec_list) #extend my_list with sec_list 
print(my_list) #[10,15,30,40,50,60,70]
my_list.pop() #removing the last element from my_list
print(my_list) #[10,15,30,40,50,60]
my_list.sort() #sorting the list in ascending order
print(my_list) #[10,15,30,40,50,60,70]
#find and print index of 30
print(my_list.index(30)) #returns 2
