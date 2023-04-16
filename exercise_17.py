"""
    Exercise - 17:  Text Alignment

   Sample Input
    5

    Sample Output

          H    
         HHH   
        HHHHH  
       HHHHHHH 
      HHHHHHHHH
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHHHHHHHHHHHHHHHHHHHHHH   
        HHHHHHHHHHHHHHHHHHHHHHHHH   
        HHHHHHHHHHHHHHHHHHHHHHHHH   
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
        HHHHH               HHHHH             
                          HHHHHHHHH 
                           HHHHHHH  
                            HHHHH   
                             HHH    
                              H 
        
    Cassio Cioni Carmo - 04/16/2023
"""
logo_thickness =int(input())
empty_space=logo_thickness * 2 - 1
center_space=int((logo_thickness + 1)/2)

for i in range(0,logo_thickness):
    first_part='H'*(i*2+1)
    print(first_part.center(empty_space," "))
    
second_part='H'* logo_thickness
    
for i in range(1,logo_thickness + 2):
    
    print( second_part.center(empty_space," ") + second_part.rjust(int((9 * logo_thickness - empty_space)/2)," "))
    
for i in range(1,center_space +1):
    center_part='H'*(5 * logo_thickness)
    print(center_part.center(6 * logo_thickness -1," "))

for i in range(1,logo_thickness + 2):
    print( second_part.center(empty_space," ") + second_part.rjust(int((9 * logo_thickness - empty_space)/2)," "))

for i in range(empty_space,0,-2):
    last_part='H'* i
    print(" "*(4 * logo_thickness)+ last_part.center(empty_space," "))
