import pensador
import json

def convert_to_dict(obj):
    """
    A function takes in a custom object and returns a dictionary representation of the object.
    This dict representation includes meta data such as the object's module and class names.
    """

    #  Populate the dictionary with object meta data
    obj_dict = {
    "__class__": obj.__class__.__name__,
    "__module__": obj.__module__
    }

    #  Populate the dictionary with object properties
    obj_dict.update(obj.__dict__)

    return obj_dict

query = pensador.Pensador()

rep1 = query.quote('amor')

with open('quote_query.json', 'w') as f:
    json.dump(rep1, f, default=convert_to_dict)


rep2 = query.author('João Guimarães Rosa')

with open('author_query.json', 'w') as f:
    json.dump(rep2, f, default=convert_to_dict)

rep3 = query.quote('eureka')

with open('quote2_query.json', 'w') as f:
    json.dump(rep3, f, default=convert_to_dict)