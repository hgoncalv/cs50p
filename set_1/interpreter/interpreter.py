import operator

def calc(x,opCHAR,y):
    operation_map = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul,
        '/': operator.truediv  # Use truediv for floating-point division
    }
    operation_function = operation_map.get(opCHAR)

    return operation_function(x,y)

expression = input("Insert expression\n")
xOPy = expression.split(" ")
print(calc(float(xOPy[0]),xOPy[1],float(xOPy[2])))
