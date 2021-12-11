import re

class Operations:
  def _add(x: int, z: int):
    return x+z
  def _subract(x: int, z: int):
    return x-z
  def _multiply(x: int, z: int):
    return x*z
  def _divide(x: int, z: int):
    return x/z
  def _fdevide(x: int, z: int):
    return x//z
  def _exponent(x: int, z: int):
    return x**z
  def _remainder(x: int, y: int):
    return x%y

class Calculator:
  def __init__(self):
    self.operations = {
      0: Operations._add,
      1: Operations._subract,
      2: Operations._multiply,
      3: Operations._divide,
      4: Operations._fdevide,
      5: Operations._exponent,
      6: Operations._remainder
    }
  def _get_operation(self, choice):
    return self.operations[choice]
  def _is_int(self, obj: str):
    return re.search('^\s*-?[0-9]{1,100}\s*$', obj)
  def start(self):
    print('Python Calculator\n0. Add\n1. Subtract\n2. Multiply\n3. Devide\n4. Floor Devide\n5. Exponent\n6. Remainder')
    operation = input('Please enter your operation [0/1/2/3/4/5/6]: ')
    if(self._is_int(operation) == None or int(operation) > 6): 
      return self.start()
    x = input('Value 1: ')
    z = input('Value 2: ')
    if(self._is_int(x) and self._is_int(z)): 
      print('Answer: ' + str(self._get_operation(int(operation))(int(x), int(z))))
    else: 
      print('Invalid Values')
    self.start()

if __name__ == '__main__':
  Calculator().start()
