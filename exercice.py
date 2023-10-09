#!/usr/bin/env python
# -*- coding: utf-8 -*-


import math
import copy


def get_maximums(numbers):
	result = []
	for elem in numbers:
		result.append(max(elem))
	# demo du prof (avec la condition que la liste a une longueur de 3)
	# result = [max(elem) for elem in numbers if len(elem) == 3]
	return result

def join_integers(numbers):
	return int("".join([str(n) for n in numbers]))

def generate_prime_numbers(limit):
	primes = []
	numbers = [i for i in range(2, limit + 1)]
	while len(numbers) != 0:
		primes.append(numbers[0])
		for i in range(len(numbers) - 1, -1, -1):
			if numbers[i] % numbers[0] == 0:
				del numbers[i]

	return primes

def combine_strings_and_numbers(strings, num_combinations, excluded_multiples):
	combinations = []
	for num in range(1, num_combinations + 1):
		if excluded_multiples is not None and num % excluded_multiples == 0:
			continue
		
		for letter in strings:
			combinations.append(letter + str(num))

	return combinations

if __name__ == "__main__":
	print(get_maximums([[1,2,3], [6,5,4], [10,11,12], [8,9,7]]))
	print("")
	print(join_integers([111, 222, 333]))
	print(join_integers([69, 420]))
	print("")
	print(generate_prime_numbers(17))
	print("")
	print(combine_strings_and_numbers(["A", "B"], 2, None))
	print(combine_strings_and_numbers(["A", "B"], 5, 2))
