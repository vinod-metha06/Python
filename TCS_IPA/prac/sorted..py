class Employee:
     
    def __init__(self, name, dept, age):
        self.name = name
        self.dept = dept
        self.age = age
 
    def __repr__(self):
        return '{' + self.name + ', ' + self.dept + ', ' + str(self.age) + '}'
 
if __name__ == '__main__':
 
    employees = [
        Employee('John', 'IT', 28),
        Employee('Sam', 'Banking', 20),
        Employee('Joe', 'Finance', 25)
    ]
 
    sortedByName = sorted(employees, key=lambda x: x.name)
    
    sortedByAge = sorted(employees, key=lambda x: x.age)
 
    # output: [{Joe, Finance, 25}, {John, IT, 28}, {Sam, Banking, 20}]
    print(sortedByName,sortedByAge)
    
    
 # For List of Tuple   
    
l=[
    (1,5,60),
    (8,5,7)
]
s=sorted(l,key=lambda x:x[2])
print(s)


    
d={

}
s=sorted(l,key=lambda x:x[2])
print(s)