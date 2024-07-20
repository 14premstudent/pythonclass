import pickle  

def write():
    f = open("my.dat","wb")
    l = []
    while True:
        r = input("Enter Your Roll No: ")
        n = input("Enter Your Name: ")
        m = input("Enter your Marks")
        l.append(f"{r} {n} {m}")
        a = input("Enter e for Exit")
        if a.lower() =='e':
            break;
    pickle.dump(l,f)
    f.close()

def read():
    f = open("my.dat","rb")
    l = pickle.load(f)
    return l

def update(l):
    f = open("my.dat","wb")
    s = input("Search with your")
    for i in l:
        a = i.split()

write()
l = read()
update(l)

# Overall Score: 36 / 70
# Anxiety/Depression Subscore: 9 / 10
# Attention Problem Subscore: 7 / 10
# Conduct Problem Subscore: 2 / 14

