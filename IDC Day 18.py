#Enforce a naming convention with a metaclass
class EnforceLowercase:
    def __new__(cls, class_name, parents, class_contents):
        for name in class_contents:
            # Ignore special methods like __init__
            if name[0] != "_" and name != name.lower():
                raise Exception("Method name '" + name + "' must be all lowercase.")
        
        # Create the class using the built-in type
        return type(class_name, parents, class_contents)

#Example that will work...
class Good(metaclass=EnforceLowercase):
    def run(self):
        print("Running")

    def stop(self):
        print("Stopping")

#Example that fails and shall raise an exception...
class Bad(metaclass=EnforceLowercase):
    def Run(self):  # Capital R — this will cause an error
        print("Running")
