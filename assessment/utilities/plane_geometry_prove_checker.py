"""
# Name:           check_answer_api/utilities/plane_geometry_prove_checker.py
# Description:
# Created by:     Martinus Alexander
# Date Created:   Dec 2, 2016
# Last Modified:  Jan 9, 2017
# Modified by:    Martinus Alexander
"""

import answer_formatter, expression_checker
import re

"""
Check the similarity between 2 plane geometry expression.
"""
def check(correct_answer, user_answer):
	#Create list of dictionary containing details of each answer given by the user.
	user_answer_details_list = []
	for user_step in user_answer:
		user_step_details = answer_formatter.split_plane_geometry_term(user_step)
		user_answer_details_list.append(user_step_details)
	#Find the corresponding user step in each correct answer
	for correct_step in correct_answer:
		#By default, correctness is False
		correct = False
		correct_step_details = answer_formatter.split_plane_geometry_term(correct_step)
		correct_step_LHS = correct_step_details['LHS']
		correct_step_RHS = correct_step_details['RHS']
		correct_step_delimiter = correct_step_details['delimiter']
		for user_step in user_answer_details_list:
			user_step_LHS = user_step['LHS']
			user_step_RHS = user_step['RHS']
			user_step_delimiter = user_step['delimiter']
			if check_step(correct_step_LHS, correct_step_RHS, correct_step_delimiter,
			              user_step_LHS, user_step_RHS, user_step_delimiter) == True:
				correct = True
				break
		#If step is not found in user step, the answer is wrong
		if not correct:
			return False
	#Else, the answer is correct
	return True

def check_step(correct_step_LHS, correct_step_RHS, correct_step_delimiter,
               user_step_LHS, user_step_RHS, user_step_delimiter):
	#Preliminary check
	#Delimiter should be the same
	if correct_step_delimiter != user_step_delimiter:
		return False
	#Number of term must be the same between LHS and RHS (but can be reversed as well)
	elif not ((len(correct_step_LHS) == len(user_step_LHS) and len(correct_step_RHS) == len(user_step_RHS)) \
			or (len(correct_step_LHS) == len(user_step_RHS) and len(correct_step_RHS) == len(user_step_LHS))):
		return False
	#Reverse LHS and RHS if needed
	if correct_step_LHS == user_step_RHS and correct_step_RHS == user_step_LHS:
		user_step_LHS, user_step_RHS = user_step_RHS, user_step_LHS
	LHS_correctness = all([check_term(correct_term, user_step_LHS) for correct_term in correct_step_LHS])
	RHS_correctness = all([check_term(correct_term, user_step_RHS) for correct_term in correct_step_RHS])
	if LHS_correctness and RHS_correctness:
		return True
	elif len(correct_step_LHS) == len(correct_step_RHS):
		#Maybe the LHS and RHS are reversed and were not detected
		user_step_LHS, user_step_RHS = user_step_RHS, user_step_LHS
		LHS_correctness = all([check_term(correct_term, user_step_LHS) for correct_term in correct_step_LHS])
		RHS_correctness = all([check_term(correct_term, user_step_RHS) for correct_term in correct_step_RHS])
		if LHS_correctness and RHS_correctness:
			return True
		else:
			return False
	else:
		return False

def check_term(required_term, user_term_list):
	for user_term in user_term_list:
		if "frac" in required_term and "frac" in user_term:
			#Process numerator and denominator
			required_term_numerator = re.findall(r'\{(.+?)\}', required_term)[0]
			required_term_denominator = re.findall(r'\{(.+?)\}', required_term)[1]
			user_term_numerator = re.findall(r'\{(.+?)\}', user_term)[0]
			user_term_denominator = re.findall(r'\{(.+?)\}', user_term)[1]
			numerator_correctness = check_term(required_term_numerator, [user_term_numerator])
			denominator_correctness = check_term(required_term_denominator, [user_term_denominator])
			if numerator_correctness and denominator_correctness:
				return True
		elif ("pi" in required_term or "degree" in required_term) and ("pi" in user_term or "degree" in required_term):
			if is_same_degree(required_term, user_term):
				return True
		elif "angle" in required_term and "angle" in user_term:
			if is_same_angle(required_term, user_term):
				return True
		elif any(x.isupper() and x.isalpha() for x in required_term) and any(x.isupper() and x.isalpha() for x in user_term):
			if is_same_side(required_term, user_term):
				return True
		else:
			if is_same_expression(required_term, user_term):
				return True
	return False

def is_same_expression(expr_1, expr_2):
	return expression_checker.check(expr_1, expr_2)

def is_same_angle(angle_1, angle_2):
	#Either or both of them are not an angle
	if "\\angle" not in angle_1 or "\\angle" not in angle_2:
		return False
	#Take the coefficient of both angle to be compared
	if angle_1.index("\\angle") != 0:
		angle_1_coefficient = angle_1[:angle_1.index("\\angle")]
		if angle_1_coefficient == "-":
			angle_1_coefficient = "-1"
		angle_1 = angle_1[angle_1.index("\\angle"):]
	else:
		angle_1_coefficient = "1"
	if angle_2.index("\\angle") != 0:
		angle_2_coefficient = angle_2[:angle_2.index("\\angle")]
		if angle_2_coefficient == "-":
			angle_2_coefficient = "-1"
		angle_2 = angle_2[angle_2.index("\\angle"):]
	else:
		angle_2_coefficient = "1"
	#Compare coefficient first
	if not is_same_expression(angle_1_coefficient, angle_2_coefficient):
		return False
	#Remove the details not needed in the angle, e.g. \\angle and space
	angle_1 = angle_1.replace("\\angle", "").replace(" ", "").replace("{", "").replace("}", "")
	angle_2 = angle_2.replace("\\angle", "").replace(" ", "").replace("{", "").replace("}", "")
	#Find if same angle
	if len(angle_1) != len(angle_2):
		return False
	#string[::-1] is reversed string.
	#Angle is same if the string is same or reversed
	elif angle_1.lower() == angle_2.lower() or angle_1.lower() == angle_2.lower()[::-1]:
		return True
	else:
		return False

def is_same_side(side_1, side_2):
	#Process the product of sides
	if len(re.split("\*|\\times|\\\cdot", side_1)) > 1 and len(re.split("\*|\\times|\\\cdot", side_2)) > 1:
		side_1_split = re.split("\*|\\times|\\\cdot", side_1)
		side_2_split = re.split("\*|\\times|\\\cdot", side_2)
		if len(side_1_split) != len(side_2_split):
			return False
		side_1_split.sort()
		side_2_split.sort()
		for i in range(len(side_1_split)):
			if is_same_side(side_1_split[i], side_2_split[i]):
				return True
		return False
	else: #Find whether coefficient exists
		#No coefficient
		if side_1[0].isalpha() and side_2[0].isalpha():
			if side_1.lower() == side_2.lower() or side_1.lower() == side_2.lower()[::-1]:
				return True
			else:
				return False
		#Coefficient exists
		elif side_1[0].isdigit() and side_2[0].isdigit():
			side_1_coefficient = ""
			side_1_component = ""
			for i in range(len(side_1)):
				if side_1[i].isalpha():
					global side_1_coefficient, side_1_component
					side_1_coefficient = side_1[:i]
					side_1_component = side_1[i:]
					break
			side_2_coefficient = ""
			side_2_component = ""
			for i in range(len(side_2)):
				if side_2[i].isalpha():
					global side_2_coefficient, side_2_component
					side_2_coefficient = side_2[:i]
					side_2_component = side_2[i:]
					break
			if not is_same_expression(side_1_coefficient, side_2_coefficient):
				return False
			elif side_1_component.lower() == side_2_component.lower() or side_1_component.lower() == side_2_component.lower()[::-1]:
				return True
			else:
				return False
		else:
			return False

def is_same_degree(degree_1, degree_2):
	degree_1 = degree_1.replace("\degree", "")
	degree_2 = degree_2.replace("\degree", "")
	return expression_checker.check(degree_1, degree_2)
