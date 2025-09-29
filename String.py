text = "   welcome to PYTHON programming 101!   "

print(repr(text))

t = text.strip()
print(repr(t))

print(t.capitalize())

print(t.upper())

print(t.lower())

print(t.title())

print(t.swapcase())

print(t.center(50, '-'))

print(t.count("o"))

print(t.replace("PYTHON", "Java"))

print(t.split())

print("|".join(t))

print("    Boolean Method    ")
print(t.startswith("welcome"))
print(t.endswith("101!"))
print(t.isalnum())
print(t.isalpha())
print(t.islower())
print(t.isupper())
print(t.isspace())

print("    String Comparisons    ")
print("Toyota" == "Toyota")
print("Toyota" != "Toyota")
print("Toyota" < "Nissan")
print("toyota" > "Toyota")

print("10" == str(10))  
print("10" != str(10))

print("    Sorting    ")
car = ["Toyota","Nissan","GMC","BMW","Audi"]
print(car)
print(sorted(car)) 
car.sort() 
print(car)

print("    Conversions    ")
num = 506
print(str(num))
print(int("506"))
print(float("50.6"))

try:
    print(int("hello"))
except ValueError:
    print("error")
