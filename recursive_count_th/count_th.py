'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):

    if word == '':
        return 0

    if len( word ) > 2:
        word = [ word , 0 ]


    if len( word[0] ) > 2:

        if word[0][0] == 't':
            print( 't' )
            if word[0][1] == 'h':
                print( 'h' )
                
                word[0] = word[0][1:]

                if type( word[ 1 ] ) == int:
                    word[ len( word ) - 1 ] += 1
                    count_th( word )
                else:
                    word = [ word , 1 ]
                    count_th( word )
            else:
                word[0] = word[0][1:]
                count_th( word )

        else:
            word[0] = word[0][1:]
            count_th( word )
    else:
        print( 'end of word' , word[1] )
        if word[0][0] == 't':
            if word[0][1] == 'h':
                
                word[0] = word[0][1:]

                if type( word[ 1 ] ) == int:
                    word[ len( word ) - 1 ] += 1
                    count_th( word )
                else:
                    word = [ word , 1 ]
                    count_th( word )
        else:
            return word[1]

    print( word )
    return word[1]

count_th( "thhtthht")