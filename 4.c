#include <stdio.h>
#include <string.h>
void main(){
    
 
    char* number1="1000000000000000000";
    char* number2="9999999999999999999";
    int i=0;
    char summation[strlen(number1+1)];
    int temp=0;
    int strArray[strlen(number1)+1];
    while(i<strlen(number1)){
        char temp1=number1[strlen(number1)-i-1];
        
        char temp2=number2[strlen(number2)-i-1];
        int sumtemp;
        if(temp>0){
             sumtemp=temp1+temp2-96+temp;
        }
        else{
             sumtemp=temp1+temp2-96;
        }
        
        if(sumtemp/10 >0){
            temp=sumtemp/10;
            //printf("%d",sumtemp % 10);
            strArray[i]=sumtemp % 10;
            if(i==strlen(number1)-1){
            //printf("%d",temp);
            strArray[i+1]=temp;
            }
            
        }
        else{
            //printf("%d",sumtemp);
            strArray[i]=sumtemp;
            
        }
        i++;
    }
    for (int i = sizeof(strArray)/sizeof(strArray[0]); i > 0; i--)
    {
        
        printf("%d",strArray[i-1]);
    }
    
    printf("\n");

    
}


