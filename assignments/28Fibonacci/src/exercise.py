
def main():
    x=int(input("Dame el número de la secuencia:"))
    a=0
    b=1
    if x>=0:
        if x==0:
            print(a)
        elif x==1:
                    print(b)
        elif x>=2:
            for i in range(x-1):
                c=a+b
                a=b
                b=c
                print(c)
        else:
            print("No numeros negativos")
    
    pass

if __name__=='__main__':
    main()
