amt=int(input("enter amount\n"))
n1000=amt//1000
amt%=1000
n500=amt//500
amt%=500
n100=amt//100
amt%=100
n50=amt//50
amt%=50
n20=amt//20
amt%=20
n10=amt//10
amt%=10
n5=amt//5
amt%=5
n2=amt//2
amt%=2
n1=amt//1
amt%=1
print("currency dinominations :-")
print("1000 ruppe note",n1000)
print("500 ruppe note",n500)
print("100 ruppe note",n100)
print("50 ruppe note",n50)
print("20 ruppe note",n20)
print("10 ruppe note and coin",n10)
print("5 ruppe coin",n5)
print("2 ruppe coin",n2)
print("1 ruppe coin",n1)



print(n1000)
