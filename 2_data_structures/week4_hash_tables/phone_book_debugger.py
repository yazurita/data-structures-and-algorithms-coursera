import phone_book_naive as pbn
import phone_book as pb
import random
import numpy as np

def gen_inp():
    type_ = random.choice(['add', 'del', 'find'])
    number = random.randint(0, 9999999)
    
    if type_ == 'add':
        n_letters = random.randint(1,15)
        letters = [*'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ']
        name = ''
        name_chars = np.random.choice(letters, n_letters)
        return [type_, number, name.join(name_chars)]
    else:
        return [type_, number]

r_pbn = 0
r_pb = 0
while r_pbn == r_pb:
    n = random.randint(0, 1e5)
    queries = []
    inputs = []
    for i in range(n):
        inp = gen_inp()
        queries.append(inp)
        inputs.append(pbn.Query(inp))
    r_pbn = pbn.process_queries(inputs)
    r_pb = pb.process_queries(inputs)

for i in range(len(r_pbn)):
    if r_pb[i] != r_pbn[i]:
        print(r_pb[i], r_pbn[i])
    
"""
print('input:')
print(queries)
print()
print('r_pbn:')
print(len(r_pbn))
print(r_pbn)
print()
print('r_pb:')
#print(len(r_pb))
print(r_pb)
"""