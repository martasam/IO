def dodawanie(a, b):
    return a + b
    
def get_info():
    print("To jest prosty program dodający dwie liczby")
    
get_info()    
l1 = int(input('Wprowadź pierwszą liczbę: '))
l2 = int(input('Wprowadź drugą liczbę: '))
print(dodawanie(l1, l2))
