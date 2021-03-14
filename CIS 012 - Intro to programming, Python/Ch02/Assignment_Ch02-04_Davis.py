seconds = input("Enter the elapsed time in seconds: ")
hrs = int(seconds)//3600
mins = (int(seconds)-(hrs*3600))//60
secs = (int(seconds)-(mins*60))%60
time = str(hrs)+":"+str(mins)+":"+str(secs)

print ()
print ("The elapsed time in seconds =", seconds)
print ()
print ("The equivalent time in hours:minutes:seconds =", time)
