def test1():


    try:
        print ('try executing')
        x  = 10/0
        print ('try executed')

    except:
        # x = 10/0
        print ('except Executed')

    finally:
        print ('finally executed')

    print ('block after except')


test1()