# def word_search(doc_list, keyword):
#     doc = keyword.lower()
#     for x in doc_list:
#         print(x)
#         if doc not in x:
#             l.append(doc)
#             #l.append(doc_list.index(doc))
#         #return [(doc_list.index(doc))]
#     print(l)   
#     return l




def word_search(doc_list, keyword):
    keyword=keyword.strip().rstrip('.').lower()
    new_list=[]
    for index, doc in enumerate(doc_list):
        for word in doc.split():
            if keyword == word.strip().rstrip('.').lower():
                new_list.append(index)
    return new_list


doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinovilles"]

word_search(doc_list,"car")


"Casino." "casino"

# "python" 
# x = "python is  String "

# print("python" in x)
