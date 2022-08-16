"""
Script to layout system for org system of dictionary and mapping

Utilize dictionary get key to avoid errors


"""

d1 = {"Name": "first dict", "desc": "something", "ref": "idk_to_what"}
d2 = {"Name": "second dict", "desc": "some", "ref": "first dict"}
d3 = {"Name": "third dict", "desc": "sometime", "ref": "first dict"}


ds = [d1, d2, d3]
drefs = []


# function to step through dictionary and find references
def dict_walker():
    # loop through each dictionary
    for d in ds:
        # loop through again for checking references
        for dx in ds:
            # if dict is referencing another... add to ref list
            if d.get("ref") == dx.get("Name"):
                print("found a reference!")
                drefs.append(f"{d['Name']} references {dx['Name']}")


dict_walker()
print(drefs)

