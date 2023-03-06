class Dir:
    def __init__(self, parent, name) -> None:
        self.parent = parent
        self.fileList = []
        self.fileListNames = []
        self.name = name
        self.size = 0
    
    def addFile(self, file):
        self.fileList.append(file)
        self.fileListNames.append(file.name)
    
class File:
    def __init__(self, name, size, parent) -> None:
        self.name = name
        self.size = size
        self.dir = parent

f = open("input.txt")
input = f.readlines()
f.close()

for x in range(len(input)):
    input[x] = input[x].strip()
    input[x] = input[x].split(" ")

rootDir = Dir(None, input[0][2])
input.pop(0)

# constructs the file manager
currentDir = rootDir
isListing = False # if a ls commnad is run
for command in input:
    if isListing:
        if command[0] == "$":
            isListing = False
        elif command[0] == "dir":
            currentDir.addFile(Dir(currentDir, command[1])) # adds the dir to the current directory
            continue
        else:
            currentDir.addFile(File(command[1], command[0], currentDir)) # adds the file to the current directory
            continue
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                currentDir = currentDir.parent # gets the Dir's parent
            elif command[2] in currentDir.fileListNames:
                index = currentDir.fileListNames.index(command[2]) # gets the index of existing directory
                currentDir = currentDir.fileList[index]
            else:
                currentDir = Dir(currentDir, command[2]) # creates a directory if the directory was never visited before or viewed
        elif command[1] == "ls":
            isListing = True

# assigns the size to each dir
sizes = []
def fileSize(dir):
    for file in dir.fileList:
        if type(file) == Dir:
            dir.size += fileSize(file)
        else:
            dir.size += int(file.size)
    if dir.size <= 100000: # if the dir is less than or equal to 100000 then add it to the answer
        sizes.append(int(dir.size))
    return int(dir.size)
    
fileSize(rootDir)

# adds up the sizes of the dirs added
total = 0
for item in sizes:
    total += item
print(total)