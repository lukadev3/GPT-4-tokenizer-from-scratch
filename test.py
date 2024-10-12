from tokenizer import get_stats, merge
from basic_tokenizer import BasicTokenizer
from gpt4_tokenizer import Gpt4Tokenizer

# Function checks

print("-----------------------------CHECKING FUNCTIONS-----------------------------")


list = [1, 2, 5, 1, 2, 6, 1, 2, 8, 9, 1, 2]
print(get_stats(list))
print(merge(list, (1, 2), 56))

print("-----------------------------BASIC TOKENIZER-----------------------------")


# Check BasicTokenizer
basic = BasicTokenizer()
print(basic.train("Ja sam Luka Ivanovic i volim data science :)", 260))
print("MERGES")
print(basic.merges)
print("DECODING")
print(basic.decode([74, 256, 115, 97, 258, 76, 117, 107, 256, 73, 118, 97, 110, 111, 118, 105, 99, 32, 105, 32, 118, 111, 108, 105, 258, 100, 97, 116, 256, 115, 99, 105, 101, 110, 99, 101, 32, 58, 41]))
print("ENCODING")
print(basic.encode("Ja sam Luka Ivanovic i volim data science :)"))

print("-----------------------------GPT4 TOKENIZER-----------------------------")
# Check Gpt4Tokenizer
gpt4_tokenizer = Gpt4Tokenizer()
print(gpt4_tokenizer.train("Ja sam Luka Ivanovic i ja sam bivsi fudbaler;volim data science :)", 260))
print("MERGES")
print(gpt4_tokenizer.merges)
print("DECODING")
print(gpt4_tokenizer.decode([[259], [258], [32, 76, 117, 107, 97], [32, 73, 118, 97, 110, 111, 118, 105, 99], [32, 105], [32, 106, 97], [258], [32, 98, 105, 118, 115, 105], [32, 
102, 117, 100, 98, 97, 108, 101, 114], [59, 118, 111, 108, 105, 109], [32, 100, 97, 116, 97], [256, 99, 105, 101, 110, 99, 101], [32, 58, 41]]))
print("ENCODING")
print(gpt4_tokenizer.encode("Ja sam Luka Ivanovic i ja sam bivsi fudbaler;volim data science :)"))
