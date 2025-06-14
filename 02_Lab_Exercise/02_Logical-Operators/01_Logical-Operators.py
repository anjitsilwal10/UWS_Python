# Logical Operators
# And: Returns True if both operands are True
# OR: Returns True if at least one operand is True
# Not Operator : Returns True if the operand is False and vice versa

age = 25;
is_in_age_range = age > 20 and age < 30;
print(is_in_age_range);
print(age >= 20 and age < 25);

# Or 
print(age > 30 or age <26);

# Not
print(not(age > 30 and age < 20));
# returns false because not is used to reverse the result.
