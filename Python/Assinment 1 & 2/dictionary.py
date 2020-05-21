
def dictionary(list_1):
    print(list_1)
    print(list_1[145])
    print(list_1.get(114))
    list_1[245] = "motorola"
    print(list_1)
    print(len(list_1))
    list_1.pop(145)
    print(list_1)
    list_1.popitem()
    print(list_1)
    list_1.update({123:"micromax",243:"blackberry",234:"ficco"})
    print(list_1)
    print(list_1.keys())
    print(list_1.values())

set1 = {114:"iphone",145:"xiomi",245:"samsung"}

dictionary(set1)
