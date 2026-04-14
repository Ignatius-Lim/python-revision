# LinkedIn Learning Python course by Joe Marini
# write files using the built-in Python file methods
#


# Open a file for writing and create it if it doesn't exist
# sample_file = open("textfile.txt", "w+") # w+ means create new file (if not exist) and write 
# sample_file.write("This is some sample texts.")
# sample_file.close()

# Open the file for appending text to the end
sample_file = open("textfile.txt", "a+") 

# write some lines of data to the file 
sample_file.write("\nThis is appended text 1.")
sample_file.write("\nThis is appended text 2.")


# close the file when done
sample_file.close()