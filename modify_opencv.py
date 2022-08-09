# open specified opencv cmake file and modify target lines

import sys
import os

class LineModifier:
    def __init__(self) -> None:
        self.signiture_line_string = "" # unique string to find line number
        self.actual_line_string = "" # line to modify
        self.updated_line_string = "" # new line content
        self.file_path = "" # file path to modify
        self.offset_from_signiture_line = 0 # target line offset from signiture line
    
    def create_linux_remove():
        linux_remove = LineModifier()
        linux_remove.file_path = "cmake/OpenCVModule.cmake"
        linux_remove.signiture_line_string = "  # For dynamic link numbering conventions"
        linux_remove.actual_line_string = "  if(NOT ANDROID)"
        linux_remove.updated_line_string = "  if(NOT ANDROID AND NOT UNIX)"
        linux_remove.offset_from_signiture_line = 1
        return linux_remove
    
    def create_windows_remove():
        windows_remove = LineModifier()
        windows_remove.file_path = "CMakeLists.txt"
        windows_remove.signiture_line_string = "  # Postfix of DLLs:"
        windows_remove.actual_line_string = "  ocv_update(OPENCV_DLLVERSION \"${OPENCV_VERSION_MAJOR}${OPENCV_VERSION_MINOR}${OPENCV_VERSION_PATCH}\")"
        windows_remove.updated_line_string = "  ocv_update(OPENCV_DLLVERSION \"\")"
        windows_remove.offset_from_signiture_line = 1
        return windows_remove

class VARS:
    linux_remove = LineModifier.create_linux_remove()
    windows_remove = LineModifier.create_windows_remove()



# read file
def read_file_as_lines(path: str):
    with open(path) as file:
        lines = file.readlines()
    return lines



# write to files
def write_file(path: str, lines: list):
    with open(path, "w") as file:
        file.writelines(lines)


def modify_line_helper(lines: list, line_modifier: LineModifier):
    
    for i in range(len(lines)):
        
        if lines[i].startswith(line_modifier.signiture_line_string):
            
            offset = line_modifier.offset_from_signiture_line
            if len(lines) > i+offset \
                 and lines[i+offset].startswith(line_modifier.actual_line_string):
                
                lines[i+offset] = lines[i+offset].replace(line_modifier.actual_line_string, line_modifier.updated_line_string)
                print("replaced: " + line_modifier.actual_line_string + " -> " + line_modifier.updated_line_string)
            elif len(lines) > i+offset \
                and lines[i+offset].startswith(line_modifier.updated_line_string):
                
                print("same string! no replacement!: " + line_modifier.updated_line_string + " -> " + line_modifier.updated_line_string)
            else:
                print("error occured! ")
                print("not replaced!: " + line_modifier.actual_line_string + " -> " + line_modifier.updated_line_string)
                raise ValueError("Source file changed! Check latest opencv version and update this script")

    return lines



def modify_line(line_modifier: LineModifier):
    actual_path = os.path.join(sys.argv[1], line_modifier.file_path)
    lines = read_file_as_lines(actual_path)
    lines = modify_line_helper(lines, line_modifier)
    write_file(actual_path, lines)


def modify_sources():
    modify_line(VARS.windows_remove)
    modify_line(VARS.linux_remove)

def print_usage():
    print("usage: modify_opencv.py <opencv_dir>")
    print("example:")
    print("python3 modify_opencv.py .")
    print("python3 modify_opencv.py opencv")

def program():
    if len(sys.argv) != 2:
        print_usage()
    else:
        modify_sources()


if __name__ == "__main__":
    program()