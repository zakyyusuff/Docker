#debuging
number = 42
assert number > 0

number = -42
assert number > 0
 #%%

number = 42
assert number > 0, f"number greater than 0 expected, got: {number}"

number = -42
assert number > 0, f"number greater than 0 expected, got: {number}"

#%%
number = 42

assert(number > 0, f"number greater than 0 expected, got: {number}")

#%%

number = 42

assert (
    number > 0 and isinstance(number, int),
    f"number greater than 0 expected, got: {number}"
)

#%% testing
from toko import price_with_discount

shoes = {"name": "Fancy Shoes", "price": 14900}
price_with_discount(shoes, 0.25)

#%%
price_with_discount(shoes, 2.0)

#%%
price_with_discount(shoes, 1)

#%% testing 1
sample = [42, 27, 40, 38]

def popped(sample, index=-1):
     item = sample.pop(index)
     return item
 
assert sample[-1] == popped(sample)
assert sample[1] == popped(sample, 1)

print(sample)