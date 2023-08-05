#Objects and Classes.
#class.
# 1) Class has Data Attributes.
# 2) Class has methods.

#objects
#An Object is an instance of a Class.
# A class is like a blueprint while an instance is a copy of the class with actual values.

class circle(object):
    def __int__(self,name,radius,color):
        print("The Radius of the" ,name, "is" ,radius, "and color is",color)

c1 = circle()
c1.__int__("c1","5cm","Red")
c1.__int__("c2","10cm","Blue")
c1.__int__("c3","15cm","Black")

