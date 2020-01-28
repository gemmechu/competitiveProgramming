class Solution:
    def gcd(self,a,b):
        if(b==0):
            return a
        return self.gcd(b, a%b)
    def fractionAddistion(self, expression:str)->str:
        f= [int(i) for i in (expression.replace('/',' ').replace('+',' +').replace('-',' -')).split()]
        
        n=len(f)-1
        denominator=1
        for i in range(len(f)):
            if i%2!=0:
                denominator*=f[i]

        
        numerator=0
        for i in range(len(f)):
            if i%2==0:
                numerator+=(denominator/f[i+1]) *f[i]
        
        gcd_ab=self.gcd(numerator,denominator)
        numerator/=gcd_ab
        denominator/=gcd_ab
        result=str(str(int(numerator))+'/'+str(int(denominator)))
        return result
        


     
      
main =Solution()
expression='5/3+1/3'
print(main.fractionAddistion(expression))


