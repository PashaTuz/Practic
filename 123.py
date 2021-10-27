# №1
import math
x  =  int ( input ( "x =" ))
if  x  %  2!=  0 :
    print ( "x непарне" )
else :
    print ( "x парне" )
if  x  %  20  ==  0 :
    print ( "кратне 20" )
else :
    print ( "x не ділиться на 20" )
print ()
x  =  int ( input ( "x =" ))
y  =  int ( input ( "y =" ))
if  x  >=  0  or  y  >=  0 :
    print ( "два додатніх" )
else :
    print ('Не додатні' )
if ( x  >=  0  and  y  >=  0 ) or ( x  <  0  and  y  <  0 ):
    print ('x і y мають однаковий знак' )
else :
    print ( 'x и y мають однаковий знак' )
x  =  int ( input ( "x =" ))
y  =  int ( input ( "y =" ))
z  =  int ( input ( "z =" ))
if  x  ==  y  ==  z :
    print ( "Те саме значення" )
else :
    print ( "інше значення" )
if ( x  !=  y ) and ( x  !=  z ) and ( y != z ):
    print ( 'Різні значення' )
else :
 if ( x  ==  y  and  x  !=  z ) or ( x  ==  z  and  x  !=  y ) or ( y  ==  z  and  y  !=  x ):
    print ( 'два значення рівні, а другого немає' )
 else:

#№2

    x1  =  int ( input ( "x1 =" ))
 y1  =  int ( input ( "y1 =" ))
 x2  =  int ( input ( "x2 =" ))
 y2  =  int ( input ( "y2 =" ))
 dis =  math.sqrt ((x1 - x2 ) ** 2  + ( y1 - y2 ) ** 2 )
 print ( dis )
incline = (y2 - y1) / (x2 - x1)
print ( incline )
if  x1  ==  x2  ==  0  or  y1  ==  y2  ==  0 :
    print ( "дві точки лежать на початковій точці, на одній полосі" )
else:
    print ( 'точки не лежать на початковій одній полосі' )
if  y1  >  y2 :
    print ( 'Перша точка вище' )
else :
    print ( 'Перша точка не вище' )
if  x1  >=  0  and  y1  >=  0 :
    print ( "Перший" )
elif  x1  <  0  <=  y1 :
    print ( "друний" )
elif  x1  <  0  and  y1  <  0 :
    print ( "Третій" )
else :
    print ( 'Четвертий' )
if  abs ( x1  +  x2 ) ==  abs ( x1 ) +  abs ( x2 ) and  abs ( y1  +  y2 ) ==  abs ( y1 ) +  abs ( y2 ):
    print ( 'Той самий квадрат' )
else :
    print ( 'Другий квадрат' )