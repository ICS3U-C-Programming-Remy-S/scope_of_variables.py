#!/usr/bin/env python3
# Created by: Remy Skelton
# Created on: Oct, 6, 2023
# This program scopes variables.

# global variable
variable_x = 20


def local_variable() -> None:
    # define local variables
    variable_x = 7
    variable_y = 19

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Local variable: {variable_x} + {variable_y} = {variable_z}")


def global_variable() -> None:
    # call global variables
    global variable_x
    variable_y = 15

    variable_x = variable_x + 1
    variable_z = variable_x + variable_y

    print(f"Global variable: {variable_x} + {variable_y} = {variable_z}")


def main() -> None:
    local_variable()
    global_variable()

    print("\nDone.")


if __name__ == "__main__":
    main()
