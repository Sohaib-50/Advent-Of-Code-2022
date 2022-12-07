class Folder:
    def __init__(self, folder_name, parent_folder) -> None:
        self.folder_name = folder_name
        self.parent_folder = parent_folder
        self.folders = []
        self.files_size = 0

    def get_size(self):
        total_size = 0
        total_size += self.files_size
        return total_size

    def add_child_folder(self, folder):
        self.folders.append(folder)

    def increment_size(self, increment):
        self.files_size += increment
        if self.parent_folder:
            self.parent_folder.increment_size(increment)

    def __repr__(self) -> str:
        return f"<Folder- {self.folder_name}, Childeren-{[f.folder_name for f in self.folders]}>"

home_folder = Folder(folder_name="/", parent_folder=None)
folders = set()
folders.add(home_folder)
folders_stack = [home_folder]
with open("ip.txt", "r") as f:
    f.readline()  # skip 1st line
    for line in f:
        line = line.strip()
        current_folder = folders_stack[-1]

        # no processing needed on line for list command
        if "$ ls" in line:
            continue

        # if directory changed
        elif "$ cd" in line:
            cd_folder = line[ line.find("$ cd") + 5 : ].strip()
            # if cd_folder == "/":
            #     folders_stack = [home_folder]
            if cd_folder == "..":
                # if len(folders_stack) > 1:
                folders_stack.pop()
            else:
                for folder in folders:
                    if (folder.folder_name == cd_folder) and (folder.parent_folder == current_folder):
                        folders_stack.append(folder)
                        break

    
        # a file or folder info line
        else:

            if "dir" in line:  # is a folder
                new_child_folder = Folder(folder_name=line[ line.find("dir") + 4 : ].strip(), parent_folder=current_folder)
                folders.add(new_child_folder)
                current_folder.add_child_folder(folder=new_child_folder)

            else:  # is a file
                file_size = int( line[ : line.find(" ")])  # slice line till before first space
                current_folder.increment_size(file_size)

ans = 0
for f in folders:
    if f.get_size() <= 100000:
        # print(f.get_size())
        ans += f.get_size()
print(ans)
