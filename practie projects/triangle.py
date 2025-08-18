
def match_case(triangle_match):

 match triangle_match:
    case 0: 
        print("     *     ")
    case 1:
        print("    ***    ")
    case 2: 
        print("   *****   ")
    case 3:
        print(" ********* ")
    case 4:
        print("***********")


for i in range(0,5):
    match_case(i)
