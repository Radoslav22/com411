#We wish to help Beep and Bop search the books.
#first function
def search (file_name):
    print("Searching...", end="")
   
    sections = []
    books = []
    
    with open(file_name) as file:
        
        for line in file:
            
            if (line.startswith("Section")):
                parts = line.split(":")
                sections.append(parts[1].replace('\n',''))
            
            else:
                books.append(line.replace('\n', ''))
    print("Done!")
    return (sections, books)
#second function
def save (file_name, data):
    print("Saving...", end="")
        
    with open(file_name, "w") as file:
            
        file.write("Section: ")
        for section in data[0]:
            file.write(f"{section},")
            
        file.write("\nBooks: ")
        for book in data[1]:
            file.write(f"{book},")

        print("Done!")

#third function 
def run ():
    data = search("data/files/txt/books.txt")
    save("data/files/txt/section-books.txt", data )

#call the third function
run()