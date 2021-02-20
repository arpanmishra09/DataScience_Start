def person(name, **data): #the ** sign means that now data will accept keyword and value
    print(name)
    for i,j in data.items(): #i and j represent the keyword and value and.items() is used to fetch data from the data
        print (i,j)

person('navin',age=23,city='mumbai',mobile=9835674)
#here we are using dictionary kindof function where we have keywords for each input so that it makes more sense