def capitalize_list_items(x):
    for i in range(len(x)):
        x[i]=x[i].capitalize()
    return x
print(capitalize_list_items(['potato', 'tomato', 'mango', 'milk','meat']))