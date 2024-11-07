from xvec_lib import vec3
from vec2 import vec2

while True:
    inp = input(">>> ")
    try:
        exec(inp)
    except Exception as error:
        print(error)