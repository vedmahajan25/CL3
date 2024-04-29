def fuzzy_union(set1, set2):
    result = {}
    for element in set1:
        result[element] = max(set1.get(element, 0), set2.get(element, 0))
    for element in set2:
        if element not in result:
            result[element] = set2[element]
    return result

def fuzzy_intersection(set1, set2):
    result = {}
    for element in set1:
        if element in set2:
            result[element] = min(set1[element], set2[element])
    return result

def fuzzy_complement(set1):
    result = {}
    for element in set1:
        result[element] = 1 - set1[element]
    return result

def fuzzy_difference(set1, set2):
    complement_set2 = fuzzy_complement(set2)
    return fuzzy_intersection(set1, complement_set2)

def cartesian_product(set1, set2):
    result = {}
    for element1 in set1:
        for element2 in set2:
            result[(element1, element2)] = min(set1[element1], set2[element2])
    return result

def max_min_composition(relation1, relation2):
    result = {}
    for (a, b) in relation1:
        for (c, d) in relation2:
            if b == c:
                result[(a, d)] = max(result.get((a, d), 0), min(relation1[(a, b)], relation2[(c, d)]))
    return result

# Example usage
set1 = {'a': 0.7, 'b': 0.5, 'c': 0.3}
set2 = {'b': 0.6, 'c': 0.4, 'd': 0.2}

print("Union:", fuzzy_union(set1, set2))
print("Intersection:", fuzzy_intersection(set1, set2))
print("Complement of set1:", fuzzy_complement(set1))
print("Difference of set1 and set2:", fuzzy_difference(set1, set2))

relation1 = {('x', 'y'): 0.8, ('y', 'z'): 0.5}
relation2 = {('y', 'w'): 0.7, ('w', 'z'): 0.4}

print("Cartesian product of relation1 and relation2:")
print(cartesian_product(relation1, relation2))

print("Max-min composition of relation1 and relation2:")
print(max_min_composition(relation1, relation2))
