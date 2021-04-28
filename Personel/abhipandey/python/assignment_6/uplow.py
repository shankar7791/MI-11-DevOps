def upperlow(c):
        a = sum(1 for i in c if i.isupper())
        b =  sum(1 for i in c if i.islower())
        
        print("No. of Upper case characters : %s \nNo. of Lower case characters : %s" % (a,b))
upperlow("Hello jarvis ")