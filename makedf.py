
import pandas as pd 
def makedf(s):
    l = s.split("\n")
    name = l[2]
    vehName = l[6]
    regNo = l[10]
    regDate = l[14]
    
    
    data = [['Name',name], ['Vehicle Name',vehName], ['Registration Number',regNo],['Registration date',regDate]] 
      
     
    df = pd.DataFrame(data, columns = ['Name', 'Age']) 
      
     
    print(df) 
