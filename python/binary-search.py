

def binary_search(lis, query):
    '''Reutns the query from the given list'''

    lis.sort() # sort the list
    lo = 0 #intialize the lo variable
    hi = len(lis) - 1 #intialize the hi variable

    while lo <= hi: # run the binary search until lo is less than hi
        mid = (lo + hi)//2 # find the mid point between lo and hi
        mid_number = lis[mid] # find the mid element of the list

        if mid_number == query: # if the mid number is the query
            return mid_number # return the mid number
        elif mid > 0 and mid_number > query: # if the mid number is not the first element of the list and is greater than the query
            hi = lis[mid - 1] #move the search space to the left
        else:
            lo = lis[mid + 1] # otherwise move the search space to the right

def main():
    '''Take the list of integers and query and return the found query from the list'''
    inp = input("Enter numbers separated by space: ") # input number list
    l = inp.split() # split input
    lis = [] 

    for item in l:              # make the list of integers
        lis.append(int(item))
    
    query = int(input("What number do you want to search for? ")) # ask for the query
    print("FOUND: ",binary_search(lis, query)) # print the query found from list
    

if __name__ == "__main__":
    main() # call the main function