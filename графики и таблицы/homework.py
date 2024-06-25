import random
import pandas as pd

# lst = ['robot'] * 10
# lst += ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI':lst})
# data.head()
# print(data)

# lst = ['robot'] * 10 + ['human'] * 10
# random.shuffle(lst)
# data = pd.DataFrame({'whoAmI': lst})
# one_hot_encoded = pd.concat([data, pd.get_dummies(data['whoAmI'],' prefix='is'')], axis=1).drop('whoAmI', axis=1) # Преобразуем 'whoAmI' в one hot кодирование
# print(one_hot_encoded.head())


lst = ['robot'] * 10 + ['human'] * 10 # Создаем исходный DataFrame уменьшив количество строк путем разбивки на два столбца
random.shuffle(lst)
data = pd.DataFrame({'whoAmI': lst})

def one_hot(column): # Создаем функцию для one hot кодирования
    unique_values = column.unique() #уникальные столбцы. Сколько уникальных параметров есть в df, столько и будет столбцов.
    return pd.DataFrame({val: column == val for val in unique_values})

encoded_data = one_hot(data['whoAmI'])
final_data = data.join(encoded_data)
final_data.drop('whoAmI', axis=1, inplace=True) # Удаляем исходный столбец 'whoAmI'
print(final_data.head())
