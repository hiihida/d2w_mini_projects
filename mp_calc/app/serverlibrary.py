def merge(array: list, p: int, q: int, r: int, byfunc) -> None:
  nleft = q - p + 1  # Number of elements in left subarray
  nright = r - q  # Number of elements in right subarray

  left_array = array[p: q + 1]  
  right_array = array[q + 1: r + 1]

  left = 0
  right = 0
  dest = p

  while left < nleft and right < nright:
    if byfunc(left_array[left]) <= byfunc(right_array[right]):
      array[dest] = left_array[left]
      left += 1
    else:
      array[dest] = right_array[right]
      right += 1
    dest += 1

  while left < nleft:
    array[dest] = left_array[left]
    left += 1
    dest += 1

  while right < nright:
    array[dest] = right_array[right]
    right += 1
    dest += 1

def mergesort_recursive(array: list, p: int, r: int, byfunc) -> None:
  if p < r:
    q = (p + r) // 2
    mergesort_recursive(array, p, q, byfunc)
    mergesort_recursive(array, q + 1, r, byfunc)
    merge(array, p, q, r, byfunc)

def mergesort(array, byfunc=None):
  mergesort_recursive(array, 0, len(array) - 1, byfunc)

class Stack:
    def __init__(self) -> None:
        self.__items: list = []
        
    def push(self, item):
        self.__items.append(item)

    def pop(self):
        if self.is_empty == False:
            val = self.__items[-1]
            self.__items.remove(val)
            return val
        return None

    def peek(self):
        if self.is_empty == False:
            return self.__items[-1]
        return None

    @property
    def is_empty(self) -> bool:
        if len(self.__items) == 0:
            return True
        return False

    @property
    def size(self):
        return len(self.__items)

class EvaluateExpression:
  valid_char = '0123456789+-*/() '
  def __init__(self, string=""):
    valid = True
    for char in string:
      if char not in EvaluateExpression.valid_char:
        valid = False
    if valid:
      self.expr = string
    else:
      self.expr = ""

  @property
  def expression(self):
    return self.expr

  @expression.setter
  def expression(self, new_expr):
    valid = True
    for char in new_expr:
      if char not in EvaluateExpression.valid_char:
        valid = False
    if valid:
      self.expr = new_expr
    else:
      self.expr = ""
      
  def insert_space(self):
    operators = "+-*/()"
    space_expr = ""
    for char in self.expr:
      if char in operators:
        space_expr += " " + char + " "
      else:
        space_expr += char
    return space_expr

  def process_operator(self, operand_stack, operator_stack):
    op = operator_stack.pop()
    right_operand = operand_stack.pop()
    left_operand = operand_stack.pop()
    if op == "+":
      operand_stack.push(left_operand + right_operand)
    elif op == "-":
      operand_stack.push(left_operand - right_operand)
    elif op == "*":
      operand_stack.push(left_operand * right_operand)
    elif op == "/":
      operand_stack.push(left_operand // right_operand)

  def evaluate(self):
    operands = "0123456789"
    operand_stack = Stack()
    operator_stack = Stack()
    expression = self.insert_space()
    tokens = expression.split()
    print(tokens)

    for char in tokens:
      if char in operands:
        operand_stack.push(int(char))
      elif char in ["+", "-"]:
        while operator_stack.is_empty is False and operator_stack.peek() not in ["(", ")"]:
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char in ["*", "/"]:
        while operator_stack.peek() in ["*", "/"]:
          self.process_operator(operand_stack, operator_stack)
        operator_stack.push(char)
      elif char == "(":
        operator_stack.push(char)
      elif char == ")":
        while operator_stack.peek() != "(" and operator_stack.is_empty is False:
          self.process_operator(operand_stack, operator_stack)
        operator_stack.pop()
    
    while operator_stack.is_empty is False:
      self.process_operator(operand_stack, operator_stack)
    return operand_stack.pop()


def get_smallest_three(challenge):
  records = challenge.records
  times = [r for r in records]
  mergesort(times, lambda x: x.elapsed_time)
  return times[:3]





