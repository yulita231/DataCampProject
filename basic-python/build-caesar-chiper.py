#build a Caesar cipher. 
# This is one of the simplest techniques to encrypt text,
# which consists of substituting each letter of the plain text 
# with the letter found at a fixed number of positions down the alphabet. 
# For example, with a shift of 5, a would be replaced by f, b by g and so on.

alphabet = 'abcdefghijklmnopqrstuvwxyz'
shift = 5
shifted_alphabet=alphabet[shift:]
print(shifted_alphabet)