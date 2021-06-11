# Python variable
#1
z = "rich"

def myfunc():
  x = "handsome"
  print("The man is " + x)
  y = "smart"
  print("The man is " + y)
myfunc()

print("the man is " + z)

#2
x, y, z = "Aku","adalah", "Kamu"
print(x,y,z)
x, y, z = z, y, x
print(x, y,z)
print( )

# python konstanta
#1
c = 418+32/40
d = 199-150*2
e = 601/41
if c < d:
  print("c is smaller than d")
else:
  print("c is greater than d")
if e < c:
  print("e is smaller than c")
else:
  print("e is greater than c")

#2
f = 60818/20-9
g = 9042001-200202
h = 1891/18+12
i = 78*21/17
if f > g:
  print("f is greater than g")
elif f == h:
  print("f and g are equal")
else:
  print("g is greater than f")
if i < h:
  print("i is smaller than h")
else:
  print("h is greater than i")

#3
print(1994 + 1899)
print(198622 - 18041)
print(1726 * 124)
print(600 / 22.7)
print(144 % 12)
print(900 ** 30)
print(169 // 13)
print( )

# Python String
#1
AB = "The power of God"
BC = "Nothing is impossible"
CA = "God is Good"
print(AB[4:16])
print(BC[11:21])
print(CA[7:11])

#2
P = "indonesia"
Q = "bhineka tunggal ika"
PQ = "PANCASILA"
print(P.upper())
print(Q.upper())
print(PQ.lower())

#3
A = "Kegagalan "
B = "adalah "
C = "keberhasilan "
D = "yang tertunda"
E = A + B + C + D
print(E)

#4
xy = 3
yz = 20
Sulitiyo = "I bought {} of the {} fastest cars in the world."
print(Sulitiyo.format(xy, yz))

#5
abc = "Mr. Jack said \"you will won\"."
cba= "Dayana said \"i love Indonesia\"."
print(abc)
print(cba)

#6
string = "Pencuri tas itu diamuk masa"
print(string)
print(string[::-1])
print( )

# Python list
#1
thislist = [90.99, 182.7, 182.6, 41, 17]
thislist.sort()
print(thislist)

#2
thislist = [90.99, 182.7, 182.6, 41, 17]
thislist.reverse()
print(thislist)

#3
thislist = ["Indonesia", "Inggris", "Irlandia", "India", "Italia"]
print(len(thislist))

#4
thislist = ["Teknik", "Kedokteran", "Ekonomi","Ilmu Budaya", "Mipa"]
thislist.remove("Mipa")
thislist.append("FISIP")
thislist[1:2] = ["Keperawatan", "Pertanian"]
print(thislist)

#5
ASEAN = "Indonesia%20Malaysia%20Singapura%20Laos%20Myanmar%20Thailand%20Brunei%20Kamboja"
list = ASEAN.split("%20")
print(list)

#6
list = ['Indonesia', 'Malaysia', 'Singapura', 'Laos', 'Myanmar', 'Thailand', 'Brunei', 'Kamboja']
string = ' '.join(list)
print(string)

#7
list = [11,12,'Budi',13,11,14,"Budi",15,14,25,67,"Budi",45,11,19,11,'Budi',6,55,90,100,11]
print(list.count(11))
print(list.count(14))
print(list.count(45))
print(list.count('Budi'))

#8
mylist = ['Piala saya yang ke '+str(y) for y in range (90,120)]
print(mylist)

#9
from collections import Counter
print(Counter(list))
print( )

# Python Dictionary
#1
thisdict = {
  "Brand": "Toyota",
  "Type" : "Kijang krista",
  "Model": "Minibus",
  "Colour" : "Silver",
  "Year": 2001
}
thisdict["Type Fuel"] = "Premium"
thisdict.pop("Type")
thisdict["Year"] = 2004
print(thisdict)

#2
thisdict = {
  "Brand": "Daihatsu",
  "Type" : "Xenia",
  "Model": "Minibus",
  "Colour" : "Red Candy",
  "Year": 2020
}
for x in thisdict.keys():
    print(x)
for x in thisdict.values():
    print(x)
print( )

# Python Def
#1
class kendaraan:
  def __init__(self, nama, tahun, merek, status):
    self.nama = nama
    self.tahun = tahun
    self.merek = merek
    self.status = status
    if (tahun <= 2021 and tahun >= 2018):
      self.status = "tergolong baru"
    else:
      self.status = "sudah lama"

  def Nama(self):
    print("Nama " + self.nama)

  def Tahun(self):
    print("Tahun " + str(self.tahun))

  def Merek(self):
    print("Merek " + self.merek)

  def Status(self):
    print("Status " + self.status)

  def print(self):
    print(self.nama + ", " + str(self.tahun) + ", " + self.merek + ", " + self.status)


p = kendaraan("Mobilio", 2017, "Honda", ".")
p.print()
d = kendaraan("Landcruiser", 2020, "Toyota", ".")
d.print()
print( )

# Python Optional Object
#1
class Car:
  pass


car1 = Car()
car2 = Car()
car3 = Car()
car4 = Car()

car1.name = "Toyota"
car1.made = "Japan"
car1.price = 500

car2.name = "Ford"
car2.made = "American"
car2.price = 1000

car3.name = "BMW"
car3.made = "Germany"
car3.price = 1500

car4.name = "Lamborghini"
car4.made = "Italy"
car4.price = 2000

print(car1.__dict__)
print(car4.__dict__)

#2
ee = 78926*14/25
ff = 1973
gg = 991+189-500
hh = 582/18*3-6
if ee > hh:
  print("ee is greather than hh")
if hh > ff:
  print("hh is smaller than ff")
if gg > ee:
  print("gg is greather than ee")

#3
az = 2*100/10
bz = 56-12+5
if bz > az:
  print("bz is greater than az")
elif az == bz:
  print("az and bz are equal")
else:
  print("az is greater than bz")
if bz < az:
  print("bz is smaller than az")
elif az == bz:
  print("az and bz are equal")
else:
  print("az is smaller than bz")

#4
cy = 418+32/40
dy = 199-150*2
ey = 601/41
if cy < dy:
  print("cy is smaller than dy")
else:
  print("cy is greater than dy")
if e < c:
  print("ey is smaller than cy")
else:
  print("ey is greater than cy")

#5
fx = 60818/20-9
gx = 9042001-200202
hx = 1891/18+12
ix = 78*21/17
if fx > gx:
  print("fx is greater than gx")
elif fx == hx:
  print("fx and gx are equal")
else:
  print("gx is greater than fx")
if ix < hx:
  print("ix is smaller than hx")
else:
  print("hx is greater than ix")
