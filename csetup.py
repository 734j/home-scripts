#!/bin/python3
import os
import sys
import subprocess

def validate_path_exists(setup_path):

    if not setup_path:
        print(f"The path is empty.")
        return False
    
    basename = os.path.basename(setup_path)
    realpath = os.path.abspath(setup_path)
    rp_no_basename = os.path.dirname(realpath)
    if(os.path.exists(rp_no_basename) == False):
        print(f"The path: \'{rp_no_basename}\' does not exist!")
        return False

    return True
    
def setup_c(setup_path):

    main_c = "#include <stdio.h>\n\nint main() {\n    return 0;\n}\n"
    Makefile = '''CC=gcc
CFLAGS_TESTBIN=-O0 -Wfatal-errors -Wall -Werror -Wextra -g3 -fsanitize=address -fsanitize=leak -Wpedantic -Wformat=2 -Wshadow -Wformat-truncation=2 -Wformat-overflow -fno-common -std=c99
CFLAGS=-O3 -flto -march=native -DNDEBUG -fomit-frame-pointer -s -static -std=c99
TARGET=main
TESTTARGET=main-TESTING
MAKEFLAGS += 
SRCS=main.c

all: release
clean:
	rm -f $(TARGET)
	rm -f $(TESTTARGET)

tests:
	$(CC) $(CFLAGS_TESTBIN) $(SRCS) -o $(TESTTARGET)

release:
	$(CC) $(CFLAGS) $(SRCS) -o $(TARGET)
'''

    if not validate_path_exists(setup_path):
        return -1

    main_name = "main.c"
    makefile_name = "Makefile"
    os.mkdir(setup_path)
    setup_path_dirname = os.path.dirname(setup_path)
    setup_path_basename = os.path.basename(setup_path)
    setup_path_dirname = os.path.abspath(setup_path_dirname)
    final_path = setup_path_dirname+"/"+setup_path_basename+"/"
    file = open(final_path+"/"+main_name, "w").write(main_c)
    file = open(final_path+"/"+makefile_name, "w").write(Makefile)
    
def setup_cpp(setup_path):

    main_c = "#include <iostream>\n\nint main() {\n    return 0;\n}\n"
    Makefile = '''CC=g++
CFLAGS_TESTBIN=-O0 -Wfatal-errors -Wall -Werror -Wextra -g3 -fsanitize=address -fsanitize=leak -Wpedantic -Wformat=2 -Wshadow -Wformat-truncation=2 -Wformat-overflow -fno-common -std=c++20
CFLAGS=-O3 -flto -march=native -DNDEBUG -fomit-frame-pointer -s -static -std=c++20
TARGET=main
TESTTARGET=main-TESTING
MAKEFLAGS += 
SRCS=main.cpp

all: release
clean:
	rm -f $(TARGET)
	rm -f $(TESTTARGET)

tests:
	$(CC) $(CFLAGS_TESTBIN) $(SRCS) -o $(TESTTARGET)

release:
	$(CC) $(CFLAGS) $(SRCS) -o $(TARGET)
'''
    
    if not validate_path_exists(setup_path):
        return -1

    main_name = "main.cpp"
    makefile_name = "Makefile"
    os.mkdir(setup_path)
    setup_path_dirname = os.path.dirname(setup_path)
    setup_path_basename = os.path.basename(setup_path)
    setup_path_dirname = os.path.abspath(setup_path_dirname)
    final_path = setup_path_dirname+"/"+setup_path_basename+"/"
    file = open(final_path+"/"+main_name, "w").write(main_c)
    file = open(final_path+"/"+makefile_name, "w").write(Makefile)
    
def choose_setup():
    print("Choose one of the options:\n   1) C\n   2) C++")
    while 1:
        user_input = input("? ").strip()
        if user_input == "1":
            return 1
        if user_input == "2":
            return 2
    
if len(sys.argv) < 2 or len(sys.argv) > 2:
    print(f"{sys.argv[0]} [DIR NAME]", file=sys.stderr)
    exit(-1);

choice = choose_setup()
argv = sys.argv
if(choice == 1):
    setup_c(argv[1])
elif (choice == 2):
    setup_cpp(argv[1])

