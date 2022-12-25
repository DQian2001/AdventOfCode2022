if __name__ == "__main__":
    with open( "input.txt" ) as file:
        data = file.read().strip().split( "\n\n" )
    
    allCalories = []
    for i in data:
        allCalories.append( sum( int( j ) for j in i.split() ) )
    allCalories.sort()
    print( allCalories[ -1 ] )
    print( sum( allCalories[ -3 : ] ) )