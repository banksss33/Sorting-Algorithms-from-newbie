#selection sorting from rookie using for and while loop
#หลักการทำงานคร่าวๆคือ ระบบจะทำการหาเลขที่น้อยที่สุดและเก็บไว้ในค่า minimum จากนั้นหาตำแหน่ง index ของเลข minimum นั้น
#และทำการลบ elements ใน index ที่ให้มาหลังจากนั้นก็เอาค่า minimum ไปใส่ไว้ใน List อีกอัน

Number = [2,9,7,8,4,5,3,1,6] #Number that need to be Sorted
SortedNumber = [] #Array For SortedNumber
length = len(Number) #find the length of Array
count = 0
index = 0

while count != length:
	minimum = Number[0] 
	for n in Number:
		if n <= minimum:
			minimum = n
	indexlocation = Number.index(minimum) #find minimum index
	Number.pop(indexlocation)#then remove elements of that index
	SortedNumber.append(minimum)#add the minimum elements to the list
	count+=1
print(SortedNumber)