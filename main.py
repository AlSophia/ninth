def sort_sentence(sentence):
    k = sentence.split()
    q=""
    for i in sorted(k,key=lambda a: len(a)):
        q =q+" " + i
    vui=q.lstrip()
    print(vui.capitalize()) 
