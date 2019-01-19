import json
import os
import random
import string
from oxwall_site.conftest import PROJECT_DIR

with open(os.path.join(PROJECT_DIR, "data", "status_data.json"), encoding="utf8") as f:
    status_data = json.load(f)


# def random_string(maxlength):
#     length = random.randint(1, maxlength)
#     cyr_symbol = ''.join([chr(l) for l in range(0x0410, 0x0460)
#                           if chr(l).isprintable()])
#     symbols = cyr_symbol + string.ascii_letters + string.digits + string.punctuation + " " * 10
#     # result = ""
#     # for _ in range(length):
#     #     result += random.choice(symbols)
#     # return result
#     return ''.join([random.choice(symbols) for _ in range(length)])
#
#
# status_data += [random_string(50) for _ in range(2)]


#if __name__ == "__main__":
    # print(random.random())
    # print(random.randint(100, 200))
    # print(random.randrange(2, 98, 2))
    # print(random.choice(status_data))
    #print(random_string(50))