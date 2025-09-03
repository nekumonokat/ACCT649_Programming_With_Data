# This function prints out the given symbol, repeated 'n' times, all on the same line
def print_a_customized_line(symbol, n):
    
    # This is a loop, it repeats something n times. You will learn about it later.
    for i in range(0, n):
        
        # This prints, but without a newline character at the end.
        # So the next thing that is printed will be on the same line, not the line below.
        print(symbol, end = "")
        
    # After the entire line is finished, then we print a newline character
    print()