glo_var = 167
def arithmetic_operation(num):
  """This function takes any number and does arithmetic operation on the number based on the value of the glo_var """
  print(glo_var + num)
  print(glo_var - num)
  print(glo_var * num)
  print(glo_var / num)

arithmetic_operation(106)

def operation_with_local_var(num):
    """This function takes any number and does arithmetic operation on the number based on the value of the glo_var """
    global local_var
    local_var = 57
    print(local_var + num)
    print(local_var - num)
    print(local_var * num)
    print(local_var / num)

operation_with_local_var(457)

def sum_num():
    #global local_var
    print(15 + local_var)
sum_num()