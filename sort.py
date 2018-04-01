import random
from random import randint
import numpy as np
from array import array
import math
import time
import sys
import hashlib 

########################################################################
#Вывод на экран
def my_print(message):
	allow = True
	if allow:
		print(message)

#Проверка массива на сортировку
def sort_check(data):
	count = np.size(data)-1
	i=0
	change=False
	while i<count:					
		if data[i] > data[i+1]:
			return False
		i += 1
		
	return True;

########################################################################
#Пузырьковая сортировка
def bubble_sort(data, count):
	i=0
	change=False
	while i<count:					
		if data[i] > data[i+1]:
			first = data[i]
			second = data[i+1]
			data[i] = second
			data[i+1] = first
			change=True
		i += 1   
		
	#Крайние элементы, уменьшаем область сортировки на 1
	count -= 1
	
	if change:
		bubble_sort(data, count)
		
	return data;
	
#Сортировка вставками
def insert_sort(data, count):
	i=0
	while i<count:
		if data[i] > data[i+1]:
			j=i
			while j>=0 and data[j] > data[j+1]:
				first = data[j]
				second = data[j+1]
				data[j] = second
				data[j+1] = first
				j -= 1
		i += 1   
		
	return data;
	
#Сортировка выбором
#last_sort_index - крайний отсортированый индекс (с которого начнем следующую итерацию)
def selection_sort(data, count, first_unsort_index=0):
	i=first_unsort_index+1
	last_min = data[first_unsort_index] #Крайнее наименьшее
	last_min_index = first_unsort_index
	while i<count+1:
		if last_min > data[i]:
			last_min = data[i]
			last_min_index = i
		i += 1
			
	if first_unsort_index < count:
		#Элемент который надо переместить на место минимального в оставшемся наборе
		data[last_min_index] = data[first_unsort_index]
		data[first_unsort_index] = last_min
		selection_sort(data, count, first_unsort_index+1)
		
	return data;
	
#Сортировка слиянием
def merge_sort(data):
	count = np.size(data)
	
	if count > 1:
		center = count // 2
		left = data[:center]
		right = data[center:]
		
		merge_sort(left)
		merge_sort(right)

		i, j, k = 0, 0, 0

		while i < np.size(left) and j < np.size(right):
			if left[i] < right[j]:
				data[k] = left[i]
				i += 1
			else:
				data[k] = right[j]
				j += 1
			k += 1

		while i < np.size(left):
			data[k] = left[i]
			i += 1
			k += 1

		while j < np.size(right):
			data[k] = right[j]
			j += 1
			k += 1
			
#Быстрая сортировка	(сортировка Хоара)
def quick_sort(nums, first, last):
	if first >= last: return
 
	i, j = first, last
	pivot = nums[random.randint(first, last)]

	while i <= j:
		while nums[i] < pivot: i += 1
		while nums[j] > pivot: j -= 1
		if i <= j:
			nums[i], nums[j] = nums[j], nums[i]
			i += 1
			j -= 1
	quick_sort(nums, first, j)
	quick_sort(nums, i, last)
########################################################################

def start(data, count):
	all_right = True
	names = []
	results = []

	#-----------------------------------------------------------------------
	name = 'bubble_sort'
	my_print(name)
	names.append(name)
	data__copy = data.copy()
	time_start = time.time()
	data__copy = bubble_sort(data__copy, count)
	dif_time = time.time()-time_start
	results.append(dif_time)
	my_print(dif_time)
	#print(data__copy)
	if sort_check(data__copy):
		my_print('Сортирован!!! :)')
	else:
		all_right = False
		my_print('Не сортирован :(')
		
	#-----------------------------------------------------------------------
	name = 'insert_sort'
	my_print(name)
	names.append(name)
	data__copy = data.copy()
	time_start = time.time()
	data__copy = insert_sort(data__copy, count)
	dif_time = time.time()-time_start
	results.append(dif_time)
	my_print(dif_time)
	#print(data__copy)
	if sort_check(data__copy):
		my_print('Сортирован!!! :)')
	else:
		all_right = False
		my_print('Не сортирован :(')
		
	#-----------------------------------------------------------------------
	name = 'selection_sort'
	my_print(name)
	names.append(name)
	data__copy = data.copy()
	time_start = time.time()
	data__copy = selection_sort(data__copy, count)
	dif_time = time.time()-time_start
	results.append(dif_time)
	my_print(dif_time)
	#print(data__copy)
	if sort_check(data__copy):
		my_print('Сортирован!!! :)')
	else:
		all_right = False
		my_print('Не сортирован :(')

	#-----------------------------------------------------------------------

	name = 'merge_sort'
	my_print(name)
	names.append(name)
	time_start = time.time()
	data__copy = data.copy()
	merge_sort(data__copy)
	dif_time = time.time()-time_start
	results.append(dif_time)
	my_print(dif_time)
	#print(data__copy)
	if sort_check(data__copy):
		my_print('Сортирован!!! :)')
	else:
		all_right = False
		my_print('Не сортирован :(')

	#-----------------------------------------------------------------------
	name = 'quick_sort'
	my_print(name)
	names.append(name)
	data__copy = data.copy()
	time_start = time.time()
	quick_sort(data__copy, 0, len(data__copy)-1)
	dif_time = time.time()-time_start
	results.append(dif_time)
	my_print(dif_time)
	#print(data__copy)
	if sort_check(data__copy):
		my_print('Сортирован!!! :)')
	else:
		all_right = False
		my_print('Не сортирован :(')

	#-----------------------------------------------------------------------
	if all_right == False:
		my_print('')
		print('--- Не все реализации алгоритмов справились... ---')
		return
	else:
		my_print('')
		my_print('+++ Все реализации алгоритмов успешно справились!!! +++')
		
	return {'names': names, 'results': results}
		
########################################################################
########################################################################
#Определить индекс минимального значения
def getMinResult(data):
	count = len(data)
	i=1
	result=data[0]
	result_index=0
	while i<count:	
		#print('result > data[i]', result, data[i])				
		if result > data[i]:
			result = data[i]
			result_index=i
		i += 1
	return {'result': result, 'index': result_index}

i=0
methods_hashs = {}
methods_results_count = {}
while i<=2:
	data = [randint(randint(0,10**2), randint((10**2)+1,10**4)) for _ in range(randint(10**3,10**4))]
	random.shuffle(data)
	count = np.size(data)-1
	sys.setrecursionlimit(count*20) #Лимит для рекурсии
	
	#print('')
	print('#############################')
	#print('beginnig data:')
	#print(count)
	#print(data)
	
	#Нахождение hash_md для набора данных 
	time_start = time.time()
	string_data = ''
	for v in data:
		string_data = string_data + str(v)
	md5=hashlib.md5() 
	md5.update(bytes(string_data,"UTF-8")) 
	hash_array = md5.hexdigest()
	print(time.time()-time_start)
	
	result = start(data, count)
	#key=0
	#while key < len(result['results']):
	#	print(result['names'][key], result['results'][key])
	#	key += 1
			
	min_result = getMinResult(result['results'])
	min_name = result['names'][min_result['index']]
	min_time = result['results'][min_result['index']]
	methods_hashs.update({hash_array: min_name})
	if min_name in methods_results_count:
		mrc_value = methods_results_count[min_name] + 1
	else:
		mrc_value = 1
	methods_results_count.update({min_name: mrc_value})
	print('min is: ', min_name, min_time)

	i += 1

########################################################################
############################ Total #####################################
########################################################################
for k, v in methods_results_count.items():
    print(k+':', v)
	
#print(methods_hashs)
#print(methods_results_count)
