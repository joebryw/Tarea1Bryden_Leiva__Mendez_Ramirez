

def capital(p):#defino la función
    a=str(p)
    if(a==p):
        if(p.lower()==p):#condicionales de la función
             return p.upper()#operación
         #resultado
        elif(p.lower!=p):#defino la función
            return "error"#operación
    elif(a!=p):
      return "error"
        #resultado
#llamo la función y defino que todo elemento introducido será una cadena
#capital(input(str("Write any character or a character string ")))



def finder(p):#defino la función
    a=str(p)
    if(a.find("w")>=0):#condicionales de la función
         return True #resultado
    elif(a.find("w")<0):#defino la función
        return False #resultado

#llamo la función y defino que todo elemento introducido será una cadena
#finder(input(str("Write any character or a character string ")))



def natural(n1,n2):#defino la función
    if(n1>0 and n2 >0):#condicionales de la función
         p=n1-n2#operación
         if(p<0):
             return "error"
         elif(p>0):
            return p
         #resultado
    elif(n1 or n2 <0):#defino la función
        if(n1<n2):
           error = "error" #resultado
           return error
        elif(n1>n2):
            return n1-n2

#llamo la función y defino que todo elemento introducido será una cadena
#natural(int(input ()),int(input()))

