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

currentDir = rootDir
isListing = False
for command in input:
    if isListing:
        if command[0] == "$":
            isListing = False
        elif command[0] == "dir":
            currentDir.addFile(Dir(currentDir, command[1]))
            continue
        else:
            currentDir.addFile(File(command[1], command[0], currentDir))
            continue
    if command[0] == "$":
        if command[1] == "cd":
            if command[2] == "..":
                currentDir = currentDir.parent # gets the Dir's parent
            elif command[2] in currentDir.fileListNames:
                index = currentDir.fileListNames.index(command[2])
                currentDir = currentDir.fileList[index]
            else:
                currentDir = Dir(currentDir, command[2])
        elif command[1] == "ls":
            isListing = True

thing = []
def fileSize(dir):
    for file in dir.fileList:
        if type(file) == Dir:
            dir.size += fileSize(file)
        else:
            dir.size += int(file.size)
    return int(dir.size)
    
fileSize(rootDir)

freeSpace = 70000000 - rootDir.size

dirs = []
def smallestDelete(dir):
    if freeSpace + dir.size >= 30000000:
        dirs.append(dir)
    for file in dir.fileList:
        if type(file) == Dir:
            smallestDelete(file)

smallestDelete(rootDir)

smallest = 100000000000
current = None
for dir in dirs:
    if dir.size < smallest:
        smallest = dir.size
        current = dir

print(current.size)

