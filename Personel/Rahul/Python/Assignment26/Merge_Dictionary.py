import collections as ct
def merge_dictionaries(color1,color2):
    merged_dict = dict(ct.ChainMap({}, color1, color2))
    return merged_dict

color1 = {"R": "Red", "B": "Black", "P": "Pink" }
color2 = {"G": "Green", "W": "White"}

print("Original dictionaries:")
print(color1, ' ', color2)

print("\n Merged dictionary:")
print(merge_dictionaries(color1, color2))


def merge_dictionaries(color1,color2,color3):
    merged_dict = dict(ct.ChainMap({}, color1, color2, color3))
    return merged_dict

color1 = {"R": "Red", "B": "Black", "P": "Pink" }
color2 = {"G": "Green", "W": "White"}
color3 = {"O": "Orange", "P": "Pink", "B": "Black"}

print("Original dictionaries:")
print(color1, ' ', color2, color3)

print("\n Merged dictionary:")
print(merge_dictionaries(color1, color2, color3))