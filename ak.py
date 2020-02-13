cnt = 0
with open("abc.txt", "r") as f:
    if "MACRO" in f.readline():
        cnt = cnt + 1
        print(" First Macro Started \n")
        if "INCR &X,&Y,&REG=AREG" in f.readline():
           print("---------MNT---------")
           print("|Name|Address in MDT|")
           print("|INCR|"+str(cnt)+"             |")
           
           match =  "MACRO"
           for line in f:
               if match in line:
                   cnt+=1
                   newmacro = f.readline()
                #    print(newmacro)
                   res =  []
                   res=newmacro.split()
                   print("| "+res[0] +"| "+str(cnt)+"            |")

                   print("---------------------")
                   break
                   
            
               


            

    
           
           
    


