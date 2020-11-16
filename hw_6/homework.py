# reading the file into a string
import regex
def main():
    dictionary = {
    "recodType": "recordType",
    "citationKey": "citationKey",
    "title": "tile",
    "author": "author",
    "year": "date",
    "date": "date",
    "location": "location"
}
    fname= input("Enter a filename: ")
    infile = open(fname, "r")
    # save the string into the data
    data = infile.read()
    #create a list
    myList = data.split("\n@")
    #print(myList)
    element = []
    #loop to split
    #entry = []
    for i in range(len(myList)):
        element = myList[i].split(",\n")
        #entrylist = entry.append(element)
        print(element)
        #cut the first two elements that don't behave like key=value
        #recordtype = element[i].split("{")
        #recordType = recordtype[0]
        #citationkey = recordtype[1] 
        for x in range(len(element)):
            for line in open('dictionary', 'r'):
                key,value = element[x].split("=")
                dictionary[element] = key, value
    print(dictionary)
            


        #for i in element:
        
        #dictionary = dictionary.append(x)
main()
