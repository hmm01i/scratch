def evenodd(n):
        zlist = list(n)
        print(zlist)
        sort = sorted(zlist,reverse=True)
        print(sort)
        backto = ''.join(sort)
        print(backto)
        return int(backto)

if __name__ == "__main__":
    numbers = "2472354"
    print(evenodd(numbers))
