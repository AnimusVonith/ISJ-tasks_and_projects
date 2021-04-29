#!/usr/bin/env python3

class Polynomial:
	
	str_rep = ""
	list_rep = []

	def derivative(self):
		holder = []
		for i in range(len(self.list_rep)):
			holder.append(self.list_rep[i]*i)
		holder = Polynomial(holder[1:])
		return holder

	def at_value(self, pos_a, pos_b=0):
		curr_sum = 0
		curr_pow_x = 1
		for i in range(len(self.list_rep)):
			curr_sum += curr_pow_x*self.list_rep[i]
			curr_pow_x *= pos_a
		if pos_b != 0:
			return self.at_value(pos_b) - curr_sum 
		return curr_sum

	def __gen_str_rep__(self, exponent, multiplier, prev_sign_part):
		x_part = number_part = sign_part = ""
		if exponent == 0:
			x_part = ""
		elif exponent == 1:
			x_part = "x"
		else:
			x_part = "x^" +str(exponent)
		if multiplier == 0: 
			return (exponent, multiplier, prev_sign_part)
		elif (abs(multiplier) == 1) and (x_part != ""):
			number_part = ""
		else:
			number_part = abs(multiplier)
		self.str_rep = str(number_part) +str(x_part) +prev_sign_part +str(self.str_rep)
		if multiplier < 0:
			sign_part = " - "
		else:
			sign_part = " + "
		return x_part, number_part, sign_part

	def __add__(self, other):
		holder = other.list_rep.copy()
		target_list = self.list_rep.copy()
		if len(self.list_rep) > len(other.list_rep):
			target_list = other.list_rep.copy()
			holder = self.list_rep.copy()
		for (n,_) in enumerate(target_list):
			holder[n] = holder[n]+target_list[n]
		return Polynomial(holder)

	def __pow__(self, exp):
		poly_sum = Polynomial(0)
		target = Polynomial(1)
		other = self.list_rep.copy()
		while exp > 0:
			for (mocnina, nasobitel) in enumerate(target.list_rep):
				for (exponent, multiplier) in enumerate(other):
					poly_sum = poly_sum + Polynomial(hackyway=str("x" +str(exponent + mocnina) +"=" +str(multiplier * nasobitel))) 
			target = poly_sum
			poly_sum = Polynomial(0)
			exp = exp-1
		return target

	def __eq__(self, other):
		return str(self.str_rep) == str(other.str_rep)

	def __init__(self, *args, **kwargs):
		
		self.str_rep = ""
		self.list_rep = []
		x_part = sign_part = "";
		if kwargs.get("hackyway", False):
			exp,mul = kwargs.get("hackyway").split("=")
			exp = int(exp[1:])
			mul = int(mul)
			_, _, sign_part = self.__gen_str_rep__(exp,mul,sign_part)
			if sign_part == " - ":
				self.str_rep = "-"+str(self.str_rep)
			for iteration in range(exp+1):
				if iteration == exp:
					self.list_rep.append(mul)
				else:
					self.list_rep.append(0)
		elif kwargs != {}:
			sorted_list = sorted([int(x[1:]) for x in list(kwargs.keys())])
			for key in sorted_list:
				_, _, sign_part = self.__gen_str_rep__(key,int(kwargs.get("x"+str(key), 0)),sign_part)
			if sign_part == " - ":
				self.str_rep = "-" +str(self.str_rep)
			for iteration in range(sorted_list[-1]+1):
				self.list_rep.append(int(kwargs.get("x"+str(iteration), 0)))
		elif args != ():
			holder = list(args)
			if type(holder[0]) is list:
				holder = holder[0]
			for (n, arg) in enumerate(holder):
				x_part, _, sign_part = self.__gen_str_rep__(int(n),int(arg),sign_part)
				self.list_rep.append(int(arg))
			if sign_part == " - ":
				self.str_rep = "-" +str(self.str_rep)
		else:
			self.str_rep = "0"
			self.list_rep = [0]
		if self.str_rep == "":
			self.str_rep = "0"
		if self.list_rep == []:
			self.list_rep = [0]
			
	def __str__(self):
		return self.str_rep

if __name__ == "__main__":
	import doctest
	doctest.testmod()
