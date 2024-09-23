from org.transcrypt.stubs.browser import *
import random

def gen_random_int(number, seed):

	random.seed(seed)
	result = random.randint(-10, 10)
	#print(result)
	return result

def generate():
	number = 10
	seed = 200
	array = []

	# call gen_random_int() with the given number and seed
	# store it to the variable array
	for i in range(number):
		array.append(gen_random_int(number, seed))
	print(array)

	# convert the items into one single string 
	# the number should be separated by a comma
	# and a full stop should end the string.
	array_str = ls_to_str(array)
	
	# This line is to placed the string into the HTML
	# under div section with the id called "generate"	
	document.getElementById("generate").innerHTML = array_str


def ls_to_str(array):
	array_str = ""

	for i in range(len(array)):
		array_str += str(array[i])
		if i == len(array)-1:
			array_str += "."
		else:
			array_str += ", "
	return array_str


def insertion_sort(array):
	n = len(array)
	
	for border_index in range(1, n):
		small_index = border_index
		while small_index > 0 and array[small_index-1] > array[small_index]:
			array[small_index-1], array[small_index] = array[small_index], array[small_index-1]
			small_index -= 1
	return array


def sortnumber1():
	'''	This function is used in Exercise 1.
		The function is called when the sort button is clicked.

		You need to do the following:
		- get the list of numbers from the "generate" HTML id, use document.getElementById(id).innerHTML
		- create a list of integers from the string of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	ls_str = document.getElementById("generate").innerHTML
	ls_int = []

	ls_str = ls_str.replace(".", ", ") # replace '.' at end of str
	ls_str = ls_str.split(", ") # separate by ", "
	ls_str = ls_str[:-1] # remove empty item in last index
	#print(ls_str)

	for i in ls_str:
		ls_int.append(int(i))
	#print(ls_int)

	sorted_array = insertion_sort(ls_int)
	array_str = ls_to_str(sorted_array)
	
	document.getElementById("sorted").innerHTML = array_str


def sortnumber2():
	# lydia test
	'''	This function is used in Exercise 2.
		The function is called when the sort button is clicked.

		You need to do the following:
		- Get the numbers from a string variable "value".
		- Split the string using comma as the separator and convert them to 
			a list of numbers
		- call your sort function, either bubble sort or insertion sort
		- create a string of the sorted numbers and store it in array_str
	'''
	# The following line get the value of the text input called "numbers"
	value = document.getElementsByName("numbers")[0].value

	# Throw alert and stop if nothing in the text input
	if value == "":
		window.alert("Your textbox is empty")
		return
	else:
		print(value)
		x = value.split(",")
		ls = []
		for i in x:
			#changed_type = int(i)
			ls.append(int(i))
		print(ls)
		sorted_list = insertion_sort(ls)

		array_str = ls_to_str(sorted_list)

		document.getElementById("sorted").innerHTML = array_str


