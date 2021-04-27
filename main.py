import time

def parametrized_decor(destination):
  def logger(func):
    def wrapper(*args, **kwargs):
      file = open(destination, "a")
      lagr = []
      for arg in args:
        lagr.append(arg)
      local_time = time.localtime()
      date_and_time = str(local_time.tm_mday) + "." + str(local_time.tm_mon) + "." + str(local_time.tm_year) + " " + str(local_time.tm_hour) + ":"
      if(local_time.tm_min < 10): 
        date_and_time += "0" + str(local_time.tm_min)
      else:
        date_and_time += str(local_time.tm_min)
      file.write("Время выполнения функции: {}".format(date_and_time) + "\n")
      file.write("Название функции: {}".format(func.__name__) + "\n")
      file.write("Аргументы и переменные функции: {}".format(lagr) + "\n")
      result = func(*args)
      file.write("Результат выполнения: {}".format(str(result)) + "\n")
      file.write("------\n")
      return result
    return wrapper
  return logger



@parametrized_decor(destination='logger.txt')
def test(a,b):
  c = a + b
  print("test")
  print(c)
  return c


test(4,2)
