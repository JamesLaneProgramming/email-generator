file_DIR = "./names.txt"

def main():
    global file_DIR
    try:
        file_Object = open(file_DIR, "r")
        generate_email(file_Object)
        file_Object.close()
    except IOError as err:
        raise err
    except EOFError as err:
        console.log("No data was read, EOFError returned")

def generate_email(file_Object):
    generated_email = None
    for each in file_Object.read().split(", "):
        print("Name: " + each)
        splitString = each.split(" ")
        newEmailString = "{0}.{1}@company_name.com".format(splitString[0], splitString[1])
        print("Generated Email: " + newEmailString)
if __name__ == '__main__':
    main()
else:
    console.log("This module is imported")
