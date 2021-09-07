def main():
    n=int(input("Escribe un numero entero:"))
    for i in range(1, n+1):
        if i%2:
            print(i,"-#")
        if not i%2:
            print(i,"-%")
    
    pass

if __name__=='__main__':   
    main()
