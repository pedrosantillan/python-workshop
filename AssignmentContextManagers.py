import copy
from contextlib import contextmanager

my_dict = {"environment": "prod", "db": "MySQL", "nums": [1, 2, 3]}

@contextmanager
def my_patch_dict(my_dict,newValues):
    copy_my_dict= copy.deepcopy(my_dict)
    my_dict['environment']=newValues['environment']+"++"
    my_dict['db'] = "MySQL++"
    my_dict['name']=newValues['name']
    my_dict['greeting'] = "Hello"
    my_dict["nums"].append(4)
    print("After Manager Process 1: ", my_dict)
    yield my_dict
    my_dict['environment'] = copy_my_dict['environment']
    my_dict['db'] = copy_my_dict['db']
    del my_dict['name']
    del my_dict['greeting']
    print("After Manager Process 2: ",my_dict)

print("Before: ",my_dict)
with my_patch_dict(my_dict,  {"environment": "testing", "name": "Marco"}):
    print()
print("After: ", my_dict)


