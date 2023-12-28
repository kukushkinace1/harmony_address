from pyhmy import util

with open('addresses.txt') as f:
    addresses = f.read().splitlines()
print('\n\n')

for address in addresses:
    one_addr = util.convert_hex_to_one(address)
    print(one_addr)
    with open(f'harmony_addresses.txt', 'a') as f:
        f.write(f'{address}:{one_addr}\n')

