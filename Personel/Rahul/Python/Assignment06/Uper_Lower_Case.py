def upperlow(c):
        u = sum(1 for i in c if i.isupper())
        l =  sum(1 for i in c if i.islower())
        
        print("Number of Upper case characters : %s \nNumber of Lower case characters : %s" % (u,l))
upperlow("Rahul Is Developer")