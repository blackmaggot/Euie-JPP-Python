__author__ = 'WiktorMarchewka'
from math import sqrt
class QuadraticEquation:
    numbers = (4, 9, 1)
    a = numbers[0]
    b = numbers[1]
    c = numbers[2]


    # def delta_calculation(self):
    #     ac = (self.a * self.c)
    #     ad = ac*4
    #     pwr = (pow(self.b, 2))
    #     delta = self.b*self.b-4*self.a*self.c #float(pwr-ad)
    #     deltasqrt = sqrt(delta)
    #     return deltasqrt #delta
    # def square_roots(self):
    #     assert self.a > 0, "a musi byc wieksze od 0"
    #     instance = QuadraticEquation()
    #     delta = float(instance.delta_calculation())
    #     component = delta
    #     if delta == 0:
    #         x12 = (-(self.b))/2*self.a
    #         print("pierwiastek rownania kwadratowego to: "+x12)
    #     elif delta != 0:
    #         x1 = (-(self.b) - component)
    #         x2 = (-(self.b) + component)
    #         print("pierwiastki rownania kwadratowego to: ", x1, " oraz ", x2)
    def delta_calculation(self):
        delta = float(pow((self.b), 2)-4*(self.a*self.c))
        print(delta)
        if delta == 0:
            x = (-(self.b))/(2*self.a)
            print(x)
        elif delta > 0:
            x1 = ((-self.b-sqrt(delta))/(2*self.a))
            x2 = ((-self.b+sqrt(delta))/(2*self.a))
            print(x1, x2)

    def sq_r(self):
        instance = QuadraticEquation()
        if instance.delta_calculation() == 0:
            x = (-(self.b))/(2*self.a)
            print(x)
        else: instance.delta_calculation()
        x1 = ((-self.b-sqrt(instance.delta_calculation()))/(2*self.a))
        print(x1)

test = QuadraticEquation()
test.delta_calculation()


