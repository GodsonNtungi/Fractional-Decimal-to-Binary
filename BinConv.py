# -*- coding: utf-8 -*-
#author Ntungi

'''convert an number with fractional part to binary'''
class binConv:
    import math
    

    def binary_frac(x,sum1=0,the_binary=''):
        x=x -  math.trunc(x)
        bin=math.trunc(x*2)
        the_binary += str(bin)
        new_val=x*2-bin
    
    
        if u==0:
            sum1 +=1
            
        if sum1>5:
            return the_binary
        
        else:
            return binary_frac(new_val,sum1,the_binary)
    
        
    def binary(x):
        bin0=str(bin(math.trunc(x)))
        bin0=bin0.split('b')
        frac=binary_frac(x)
        
        binary1=bin0[1]+'.'+frac
        return binary1
    
    
        
