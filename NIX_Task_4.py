"""
 TASK_4: Format price in list.
Дан список из строк. Создайте однострочное решение (при помощи list comprehension),
которое приведёт к верхнему регистру все строки, содержащие слово 'price')
"""

m_list = [i.upper() if 'price' in i else i for i in ['Python 3', 'MySQL', 'SSDprice', 'Linux_price', 'https']]
print('m_list: ', m_list)
