from isj_proj5_xadamc07 import gen_quiz

def test1():
    
    test_qpool1 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4', 
        ['Answer1', 'Answer2'])]

    existing_quiz1 = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2'])]

    expected = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2']), 
    ('Question3', 
        ['10: Answer1', '20: Answer2', '30: Answer3']), 
    ('Question1', 
        ['10: Answer1', '20: Answer2', '30: Answer3'])]
    assert(gen_quiz(test_qpool1, -2, 0, altcodes = ('10', '20', '30'), quiz = existing_quiz1) == expected)

'''----------------------------------------------------------------------------------------------------------------'''

def test2():

    test_qpool2 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4',
        ['Answer1', 'Answer2'])]

    existing_quiz2 = [
    ('ExistingQuestion1',
        ['1: Answer1', '2: Answer2', '3: Answer3']),
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2'])]

    not_used = gen_quiz(test_qpool2, -2, 0, altcodes = ('1', '2', '3'), quiz = existing_quiz2)

    expected = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2']), 
    ('Question3', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('Question1', 
        ['1: Answer1', '2: Answer2', '3: Answer3'])]

    assert(existing_quiz2 == expected)

'''----------------------------------------------------------------------------------------------------------------'''

def test3():

    test_qpool3 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4', 
        ['Answer1', 'Answer2'])]

    existing_quiz3 = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2'])]

    not_used1 = gen_quiz(test_qpool3, 0, 2, altcodes = ('i', 'ii', 'iii'), quiz = existing_quiz3)

    not_used2 = gen_quiz(test_qpool3, 1, altcodes = ('i', 'ii', 'iii'), quiz = existing_quiz3)

    expected = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2']), 
    ('Question1', 
        ['i: Answer1', 'ii: Answer2', 'iii: Answer3']), 
    ('Question3', 
        ['i: Answer1', 'ii: Answer2', 'iii: Answer3']), 
    ('Question2', 
        ['i: Answer1', 'ii: Answer2', 'iii: Answer3'])]

    assert(existing_quiz3 == expected)

'''----------------------------------------------------------------------------------------------------------------'''

def test4():

    test_qpool4 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4', 
        ['Answer1', 'Answer2'])]
    
    expected = [
    ('Question1', 
        ['A: Answer1', 'B: Answer2', 'C: Answer3', 'D: Answer4']), 
    ('Question2', 
        ['A: Answer1', 'B: Answer2', 'C: Answer3']), 
    ('Question4', 
        ['A: Answer1', 'B: Answer2'])]

    assert(gen_quiz(test_qpool4, 0, 1, -1) == expected)

'''----------------------------------------------------------------------------------------------------------------'''

def test5():

    test_qpool5 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4', 
        ['Answer1', 'Answer2'])]

    not_used = gen_quiz(test_qpool5, 0, altcodes = '123456')

    expected = [
    ('Question1', 
        ['1: Answer1', '2: Answer2', '3: Answer3', '4: Answer4'])]

    assert(gen_quiz(test_qpool5, 0, altcodes = '123456') == expected)

'''----------------------------------------------------------------------------------------------------------------'''

def test6():

    test_qpool6 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4', 
        ['Answer1', 'Answer2'])]

    existing_quiz6 = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2'])]

    expected = [
    ('ExistingQuestion1', 
        ['1: Answer1', '2: Answer2', '3: Answer3']), 
    ('ExistingQuestion2', 
        ['1: Answer1', '2: Answer2'])]
    
    assert(gen_quiz(test_qpool6, quiz = existing_quiz6) == expected)

'''----------------------------------------------------------------------------------------------------------------'''

def test7():

    test_qpool7 = [
    ('Question1', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question2', 
        ['Answer1', 'Answer2', 'Answer3']), 
    ('Question3', 
        ['Answer1', 'Answer2', 'Answer3', 'Answer4']), 
    ('Question4', 
        ['Answer1', 'Answer2'])]

    expected = [
    ('Question1', 
        ['101: Answer1', '201: Answer2']), 
    ('Question3', 
        ['101: Answer1', '201: Answer2'])]

    assert(gen_quiz(test_qpool7, 0, 4, 2, altcodes = ['101','201']) == expected)
    #Ignoring index 4 - list index out of range


def test_all():
    test_list=[test1, test2, test3, test4, test5, test6, test7]
    for n, test in enumerate(test_list):
        print("test "+str(n)+" running now.")
        test()
        print("test complete.")
