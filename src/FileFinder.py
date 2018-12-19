def all_txps_in_2020Model():
    import glob
    a =glob.glob('/test/*.txt')
    print(a)
    print(type(a))
    b=[i[6:]for i in a]
    return (b)
