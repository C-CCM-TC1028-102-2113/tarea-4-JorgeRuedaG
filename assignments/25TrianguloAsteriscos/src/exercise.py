
def main():
    a=int(input("Dame la altura:"))
    b=a
    for i in range(a):
        b=b-1
        c="*"*(i+1)
        print(" "*b+c)
    pass


if __name__=='__main__':
    main()
