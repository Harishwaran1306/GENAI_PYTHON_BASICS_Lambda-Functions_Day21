#Lambda Functions
#Mathematical Operations:


'''Add = lambda a,b,c: (a+b+c)
print('Addition:', Add(150,80,100))

Sub = lambda a,b,c: (a-b-c)
print('Subtraction:', Sub(150,80,90))

Multi = lambda a,b,c: (a*b*c)
print('Multiplication:', Multi(15,8,9))

Div = lambda a,b: (a//b)
print('Division:', Div(15,3))

mod = lambda a,b: (a%b)
print('Modulus:', mod(15,3))

op = lambda a,b,c,d,e: ((a+b)*(c//d)-e)
print('op:', op(40,10,15,6,3))

square = lambda a: a**2
print('Square:', square(8))

Cube = lambda a: a**3
print('Cube:', Cube(5))'''



#Map():

# Calculating the Food Price hike using Map()

'''Normal_Food_Price = {'Veg Biriyani' : '240', 'Panner Butter Masala': ' 350', 'Naan':'70', 'Butter Naan' : '80'}

New_Food_Price = dict(map(lambda item: (item[0], round(float(item[1].strip()) * 1.025)), Normal_Food_Price.items()))
print(New_Food_Price)'''



# Calculating the usd money to inr.

'''USD_Money = [650, 600, 850, 900]

INR = list(map(lambda conv: (conv*89), USD_Money))
print('Inr conversion:', INR)'''




#Filter():

#Checking the Highest reading of the machine:
'''Sensor_Readings = [105, 107, 110, 117, 118, 129, 130, 131]

High_Readings = list(filter(lambda readings: readings >= 110, Sensor_Readings))
print('High Reading in Machinery : ' , High_Readings)'''




#Filtering CSK Winner Seasons using filter()

'''csk_match_year = {'2008': 'Runner-up','2009': 'Semi-finalist',
    '2010': 'Winner',
    '2011': 'Winner',
    '2012': 'Runner-up',
    '2013': 'Runner-up',
    '2014': 'Playoffs (3rd)',
    '2015': 'Runner-up',
    '2016': 'Suspended',
    '2017': 'Suspended',
    '2018': 'Winner',
    '2019': 'Runner-up',
    '2020': 'League Stage (7th)',
    '2021': 'Winner',
    '2022': 'League Stage (9th)',
    '2023': 'Winner',
    '2024': 'League Stage (5th)',
    '2025': 'League Stage (10th)'
}

Matches_Won = list(filter(lambda year: csk_match_year[year] =='Winner', csk_match_year))
print('CSK IPL win :', Matches_Won)'''



#Sorted()
#Sorting Playing 11 by Jersey Number using sorted() and lambda:

'''players = [
    ("Abhishek Sharma", 4),
    ("Sanju Samson", 9),
    ("Ishan Kishan", 32),
    ("Shreyas Iyer", 41),
    ("Tilak Varma", 72),
    ("Shivam Dube", 25),
    ("Naman Dhir", 29),
    ("Axar Patel", 20),
    ("Kuldeep Yadav", 23),
    ("Mayank Yadav", 36),
    ("Arshdeep Singh", 2)
]

Playing_11 = sorted(players, key=lambda a: a[1])
print(Playing_11)'''





#Sorting Employees by Name using sorted() and lambda:
'''Employees = [
    {'Name' : 'Charles', 'Designation' : 'Senior Manager'},
    {'Name' : 'Van Victor', 'Designation' : 'Director'},
    {'Name' : 'Alfanso', 'Designation' : 'Manager'},
    {'Name' : 'Steve', 'Designation' : 'Team Lead'},
    {'Name' : 'Mitchel', 'Designation' : 'Engineer'},
    {'Name' : 'Bruce', 'Designation' : 'Techinal Director'},
    ]

sort = sorted(Employees, key=lambda Emp: Emp['Name'])
print(sort)'''



#Reduce():

'''from functools import reduce


A= [2,4,6,8,10,12,14,16,17,18,20]

B = reduce(lambda a,b: a-b, A)
print('Value of B:', B)

C = reduce(lambda a,b: a+b, A)
print('Value of C:', C)

D = reduce(lambda x,y: x if x<y else y, A)
print('Value of D:', D)


E = reduce(lambda x,y: x if x>y else y, A)
print('Value of E:', E)'''




                      












