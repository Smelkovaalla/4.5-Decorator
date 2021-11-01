from datetime import datetime, date, time
import time
from collections import OrderedDict



def parametrized_decor(parameter):
  def decor(foo):
    def new_foo(*args, **kwargs):
      print(datetime.now())
      print(f'Имя функции - {foo.__name__}')
      if args is not None:
        print(f'Позиционные аргументы args - {args}')
      if kwargs is not None:
        print(f'Именованные аргументы kwargs - {kwargs}')
      print("____" * 10)
      result = f'Итоговое значение {foo(*args, **kwargs)}'
	f.write(f'Путь к файлу с логами {parameter}\n')
      return result
    return new_foo
  return decor


@parametrized_decor(parameter=None)
def foo(*args, **kwargs):
	print(*args, **kwargs)


if __name__ == '__main__':
  foo(1, 2)
  
  print("____" * 20)

  documents_list = [{
      "type": "passport",
      "number": "2207 876234",
      "name": "Василий Гупкин"
  }, {
      "type": "invoice",
      "number": "11-2",
      "name": "Геннадий Покемонов"
  }]

  @parametrized_decor(parameter=None)
  def give_name(doc_list, num):
    for doc_dict in doc_list:
      if num == doc_dict['number']:
        print(
            f"Документ под номером {num} соответствует имени {doc_dict['name']}"
        )
    return

  give_name(documents_list, '11-2')
