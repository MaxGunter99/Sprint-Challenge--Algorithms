#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(n)

You are setting A to equal N * N at the en of the first while loop so it cancels out 2 ns from a < N * N * N


b)  0(n)

it will run until its reaches the n number



c) O( log n)

The finction will be called the number of digits in the number

## Exercise II

function takes in ( not broken egg , floor number ):

    if egg is not broken egg:
        floor += 1
        recursively call function with ( not broken egg , incrementing floor number )

    elif egg is broken egg:
        return floor number

calling function with ( not broken egg , floor 0 )
