import re #import regux
'''
This function is simulation for Madlib game 
the user must insert values as recommended to mix them and output funny string
read_template: to handle not found error
parse_template: to parse string to string with empty carly braces and there contenet
merge: to merge the user inputes
video_game: to connect every thing as a vedio game

'''



def read_template(path): # NotFoundErrorHandler
    try:
        with open(path) as f :
            return f.read()
    except:
        raise FileNotFoundError


def parse_template(s):
    w=re.findall("{(.*?)}",s) # to extract all data inside carly brases 
    x=re.sub("{.+?}","{}",s)  # to to extract all data inside carly brases and replacing them with {}
    # print(w)
    return x,tuple(w)

parse_template("HiToqa is {cool} and {amazing} girl")
    



def merge(s,t):
    
   return s.format(*t)


# merge("hello from {]{} the other side",["cool","amazing"])
    
def video_game(test3):
    print("**welcome to madlibs game**\n**you have to enter some word**")
    d=[]
    with open(test3) as f :
        p=parse_template(f.read())
        # print(p[1])
    for i in range(len(p[1])):
        t=input(f"{p[1][i]} ==>  ") #to input values for tuple2
        d.append(t)
       
      
    h=tuple(d)
    
    a =merge(p[0],h) #to merge both tuples
   
    with open("assets/text2.txt","w") as response:
       response.write(a)
    with open("assets/text2.txt") as response:
        f=response.read()
        print(f)





if __name__=="__main__":
    video_game("assets/text3.txt")
