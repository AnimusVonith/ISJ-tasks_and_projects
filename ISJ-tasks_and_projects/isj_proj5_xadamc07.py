#!/usr/bin/env python3

def gen_quiz(qpool, *args, **kwargs):
    holder=kwargs.get("quiz", [])
    for index in args:
        try:
            answer_holder=[]
            if kwargs.get("altcodes", False):
                for alt,ans in zip(kwargs.get("altcodes", []),qpool[index][1]):
                    answer_holder.append(str(alt)+": "+str(ans))
            else:
                for n,ans in zip(enumerate(qpool[index][1]),qpool[index][1]):
                    answer_holder.append(chr(65+n[0])+": "+str(ans))
            holder.append((qpool[index][0], answer_holder))
        except Exception as e:
            print("Ignoring index "+str(index)+" - list index out of range")
    if kwargs.get("quiz", False):
        quiz = holder
    return holder
"""
if __name__ == '__main__':
    try:
        import isj_test_proj5 as isj
        isj.test_all()
        print("test done")
    except Exception as e:
        print("test failed")
        exit(1)
    exit(0)
"""
if __name__ == "__main__":
    import doctest
    doctest.testmod()