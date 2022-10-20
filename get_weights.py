from index import get_weight
print("Enter the compound seperated by spaces: ")
compound = input()
compound_elements = compound.split()
compound_weight = get_weight(compound_elements)

print(compound_weight)