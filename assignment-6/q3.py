# inches, feet, yards, miles, kilometers, meters, centimeters, and millimeters.
class converter():
    num=0
    string=' '
    choice=''
    def __init__(self,num,string):
        self.num=num
        self.string=string
    
    def feet(self):
        if(self.string=="inches"):
            ans=self.num/12
            print( ans)
        if(self.string=="yards"):
             ans=self.num*3
             print( ans)
        if(self.string=="miles"):
            ans=self.num*5280
            print( ans)
        if(self.string=="metres"):
            ans=self.num*3.280
            print( ans)
        if(self.string=="kilometers"):
            ans=self.num*3280.84
            print( ans)
        if(self.string=="centimeters"):
            ans=self.num/30.48
            print( ans)    
        if(self.string=="millimeters"):
            ans=self.num/304.8
            print( ans)
    def inches(self):
        if(self.string=="feet"):
            ans=self.num-12
            print( ans)
        if(self.string=="yards"):
            ans=self.num*36
            print( ans)
        if(self.string=="miles"):
            ans=self.num*63360
            print( ans)
        if(self.string=="metres"):
            ans=self.num*39.3701
            print( ans)
        if(self.string=="kilometers"):
            ans=self.num*39370.08
            print( ans)
        if(self.string=="centimeters"):
            ans=self.num/2.54
            print( ans)    
        if(self.string=="millimeters"):
            ans=self.num/25.4
            print( ans)
    def yards(self):
        if(self.string=="feet"):
            ans=self.num/3
            print( ans)
        if(self.string=="inches"):
            ans=self.num/36
            print( ans)
        if(self.string=="miles"):
            ans=self.num*1760
            print( ans)
        if(self.string=="metres"):
            ans=self.num*1.09361
            print( ans)
        if(self.string=="kilometers"):
            ans=self.num*1093.61
            print( ans)
        if(self.string=="centimeters"):
            ans=self.num/91.44
            print( ans)    
        if(self.string=="millimeters"):
            ans=self.num/914.4
            print( ans)
    def miles(self):
        if(self.string=="feet"):
            ans=self.num/5280
            print( ans)
        if(self.string=="yards"):
            ans=self.num*36
            print( ans)
        if(self.string=="inches"):
            ans=self.num*1760
            print( ans)
        if(self.string=="metres"):
            ans=self.num*1609.34
            print( ans)
        if(self.string=="kilometers"):
            ans=self.num*1.60934
            print( ans)
        if(self.string=="centimeters"):
            ans=self.num/160934
            print( ans)    
        if(self.string=="millimeters"):
            ans=self.num/1609344
            print( ans)
    def kilometres(self):
        if(self.string=="feet"):
            ans=self.num/3280.84
            print( ans)
        if(self.string=="yards"):
            ans=self.num/1093.61
            print( ans)
        if(self.string=="miles"):
            ans=self.num*1.60934
            print( ans)
        if(self.string=="metres"):
            ans=self.num*1000
            print( ans)
        if(self.string=="inches"):
            ans=self.num*39370.1
            print( ans)
        if(self.string=="centimeters"):
            ans=self.num/100000
            print( ans)    
        if(self.string=="millimeters"):
            ans=self.num/1000000
            print( ans)
    def metres(self):
        if(self.string=="feet"):
                ans=self.num*0.3048
                print( ans)
        if(self.string=="yards"):
                ans=self.num*0.9144
                print( ans)
        if(self.string=="miles"):
                ans=self.num*1609.34
                print( ans)
        if(self.string=="inches"):
                ans=self.num*0.0254
                print( ans)
        if(self.string=="kilometers"):
                ans=self.num*1000
                print( ans)
        if(self.string=="centimeters"):
                ans=self.num/100
                print( ans)    
        if(self.string=="millimeters"):
                ans=self.num/1000
                print( ans)
    def centimeters(self):
        if(self.string=="feet"):
                ans=self.num*30.48
                print( ans)
        if(self.string=="yards"):
                ans=self.num*91.44
                print( ans)
        if(self.string=="miles"):
                ans=self.num*160934
                print( ans)
        if(self.string=="metres"):
                ans=self.num*100
                print( ans)
        if(self.string=="kilometers"):
                ans=self.num*100000
                print( ans)
        if(self.string=="inches"):
                ans=self.num*2.54
                print( ans)    
        if(self.string=="millimeters"):
                ans=self.num*25.4
                print( ans)  
    def millimetres(self):
        if(self.string=="feet"):
                ans=self.num*304.8
                print( ans)
        if(self.string=="yards"):
                ans=self.num*914.4
                print( ans)
        if(self.string=="miles"):
                ans=self.num*1609344
                print( ans)
        if(self.string=="metres"):
                ans=self.num*1000
                print( ans)
        if(self.string=="kilometers"):
                ans=self.num*1000000
                print( ans)
        if(self.string=="centimeters"):
                ans=self.num*10
                print( ans)    
        if(self.string=="inches"):
                ans=self.num*25.4
                print( ans)
c=converter(9,'inches')
c.feet()
c.millimetres()