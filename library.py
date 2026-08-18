class Greeting:
  @staticmethod
  def morning(name):
    return f"Good Morning {name}"
    
  @staticmethod  
  def afternoon(name):
    return f"Good Afternoon {name}"
    
  @staticmethod  
  def evening(name):
    return f"Good Evening {name}"
    
  @staticmethod
  def night(name):
    return f"Good Night {name}"


class Math:
  @staticmethod
  def CtoF(c):
    return (f"{(c * (9/5)) + 32}⁰F")
    

  def FtoC(f):
    #return (f"{(f-32)*(5/9)}⁰C")
    return (f"{(5*(f-32)/9)}")
    
    
    
    


    


m = Math
print(m.FtoC(-40))





g = Greeting    
print(g.evening("miraj"))

#if __name__=="__main__":
#    main()
