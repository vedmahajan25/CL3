import Pyro4

uri = "PYRO:obj_71ac604d2db14747b99cb6540114f900@localhost:53322"
string_concatenator = Pyro4.Proxy(uri)

str1 = "Hello, "
str2 = "World!"
result = string_concatenator.concatenate_strings(str1, str2)
print("Concatenated String:", result)
