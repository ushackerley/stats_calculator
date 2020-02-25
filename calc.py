# Calculator
from math import factorial, exp, sqrt
import scipy.stats as st
import pandas as pd

def convert_to_float(frac_str):
	"""This function converts strings to floats, even if they are written as fractions."""
	
	try:
		return float(frac_str)
	except ValueError:
		num, denom = frac_str.split('/')
		try:
			leading, num = num.split(' ')
			whole = float(leading)
		except ValueError:
			whole = 0
		frac = float(num) / float(denom)
		return whole - frac if whole < 0 else whole + frac


def contents():
	""" This function provides the contents required to call various calculators from the calculators function."""
	calculator = input("""Which calculator would you like to use?:
		[1] Poisson Calculator
		[2] Poisson Cumulative Calculator
		[3] Poisson Reverse Cumulative Calculator (p(r >= a))
		[4] Binomial Calculator
		[5] Binomial Cumulative Calculator
		[6] Binomial Reverse Cumulative Calculator
		[7] Standard Normal Cumulative Calculator (get p-values)
		[8] Inverse Standard Normal Cumulative Calculator (get z-values)
		[9] chi2 Cumulative Calculator
		[10] chi2 Percent point function
		[11] Student's t distribution ppf
		[12] Pearson Product Moment Correlation Coefficient ppf
		[13] Spearman Rank Correlation Coefficient ppf
		[14] F-distribution ppf
		[q] Quit
		""")
	calculators(calculator)
	pass


def calculators(calculator):
	""" This function provides a set of standard statistical calculators, chosen from the contents function."""
	result_string = 'The answer is: '

	if calculator == '1':
		# Poisson
		lam = convert_to_float(input("What is the mean, or mean times time? "))
		r = int(input("What is the random variable? "))
		po = ((lam) ** r * exp(- lam)) / factorial(r)
		print(result_string, round(po, 4))

	elif calculator == '2':
		# Cumulative Poisson
		lam = convert_to_float(input("What is the mean, or mean times time? "))
		r = int(input("What is the random variable? "))
		cdpo = 0
		for rv in range(0,r+1):
			cdpo += ((lam) ** rv * exp(- lam)) / factorial(rv)
		print(result_string, round(cdpo, 4))

	elif calculator == '3':
		# Reverse cumulative Poisson
		lam = convert_to_float(input("What is the mean, or mean times time? "))
		r = int(input("What is the random variable? "))
		cdpo = 0
		for rv in range(0,r):
			cdpo += ((lam) ** rv * exp(- lam)) / factorial(rv)
		print(result_string, round(1-cdpo, 4))

	elif calculator == '4':
		# Binomial
		n = int(input("What is the number of trials? "))
		q = convert_to_float(input("What is the probability of success? "))
		r = int(input("What is the number of successes? "))
		bino = factorial(n) / (factorial(r) * factorial(n-r)) * q ** r * (1-q) ** (n-r)
		print(result_string, round(bino, 4))

	elif calculator == '5':
		# Cumulative binomial
		n = int(input("What is the number of trials? "))
		q = convert_to_float(input("What is the probability of success? "))
		r = int(input("What is the random variable? "))
		cdbino = 0
		for rv in range(0,r+1):
			cdbino += factorial(n) / (factorial(rv) * factorial(n-rv)) * q ** rv * (1-q) ** (n-rv)
		print(result_string, round(cdbino, 4))

	elif calculator == '6':
		# Reverse cumulative binomial.
		n = int(input("What is the number of trials? "))
		q = convert_to_float(input("What is the probability of success? "))
		r = int(input("What is the random variable? "))
		cdbino = 0
		for rv in range(0,r):
			cdbino += factorial(n) / (factorial(rv) * factorial(n-rv)) * q ** rv * (1-q) ** (n-rv)
		print(result_string, round(1-cdbino, 4))

	elif calculator == '7':
		# Return a p value given a z value. Standard normal p-values.
		z = convert_to_float(input("What is the z value? "))
		p_value = st.norm.cdf(z)
		print(result_string, round(p_value, 4))

	elif calculator == '8':
		# Returning z values given a p value. Standard normal critical value.
		p_value = convert_to_float(input("What is the p value? "))
		z = st.norm.ppf(p_value)
		print(result_string, round(z, 4))

	elif calculator == '9':
		# Cumulative chi squared. p-values
		df = int(input("What are the degrees of freedom? "))
		x = convert_to_float(input("What is the x-value to which you are cumulating (i.e. the X^2 value? "))
		chi2cum = st.chi2.cdf(x, df)
		print(result_string, round(chi2cum,3))

	elif calculator == '10':
		# chi squared critical value
		df = int(input("What are the degrees of freedom? "))
		p_value = convert_to_float(input("What is the cumulation area for which you would like the x-value? "))
		chi2ppf = st.chi2.ppf(p_value, df)
		print(result_string, round(chi2ppf, 3))

	elif calculator == '11':
		# Student's t critical value
		df = int(input("What are the degrees of freedom? "))
		p_value = convert_to_float(input("What is the cumulation area for which you would like the x value? "))
		studentppf = st.t.ppf(p_value, df)
		print(result_string, round(studentppf, 3))

	elif calculator == '12':
		# Pearson critical value
		n = int(input("What are the degrees of freedom? "))
		p_value = convert_to_float(input("What is the cumulation area for which you would like the x-value? "))
		t = st.t.ppf(p_value, n-2)
		r = t / sqrt((n-2 + t ** 2))
		print(result_string, round(r, 4))

	elif calculator == '13':
		# Spearman rank critical value up to dims 17
		n = int(input("What are the degrees of freedom? "))
		p_value = convert_to_float(input("Which two-tailed p_value would you like? (double sig-level for one-tailed) [0.1, 0.05, 0.025]: "))
		spearman_table = pd.read_csv('./spearman.csv', index_col=0)
		x = spearman_table.loc[n, '{}'.format(p_value)]
		print(result_string, round(x, 4))

	elif calculator == '14':
		# F-distribution given degrees of freedom and p-value
		n1 = convert_to_float(input("What is the first degree of freedom? "))
		n2 = convert_to_float(input("What is the second degree of freedom? "))
		p_value = convert_to_float(input("What is cumulation value? (two tailed significance levels should be halved) "))
		f = st.f.ppf(p_value, n1, n2)
		print(result_string, round(f, 4))

	elif calculator == 'q':
		# To exit the calculator.
		print("Type contents() to return to calculator.")
		return 0
	
	else:
		print("I don't understand")

	print('')
	contents() # Unless we quit, this will bring us back to the contents each time.
	pass


contents() # This calls the function initially.
