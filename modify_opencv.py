# open specified opencv cmake file and modify target lines


from asyncore import write


class VARS:
    opencv_cmake_module_path = "opencv/cmake/OpenCVModule.cmake"
    target_line_sign = "  # For dynamic link numbering conventions"
    actual_line = "  if(NOT ANDROID)"
    updated_line = "  if(NOT ANDROID AND LINUX)"



# read file
def read_file_as_lines():
    with open(VARS.opencv_cmake_module_path) as file:
        lines = file.readlines()
    return lines



# write to files
def write_file(lines: str):
    with open(VARS.opencv_cmake_module_path, "w") as file:
        file.writelines(lines)


def modify_file(lines):
    for i in range(len(lines)):
        if lines[i].startswith(VARS.target_line_sign):
            if len(lines) > i+1 and lines[i+1].startswith(VARS.actual_line):
                lines[i+1] = lines[i+1].replace(VARS.actual_line, VARS.updated_line)
                print("replaced: " + VARS.actual_line + " -> " + VARS.updated_line)

    return lines


def program():
    lines = read_file_as_lines()
    lines = modify_file(lines)
    write_file(lines)


if __name__ == "__main__":
    program()