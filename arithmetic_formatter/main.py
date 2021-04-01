# This entrypoint file to be used in development
from arithmetic import arithmetic
from unittest import main


print(arithmetic(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))


# Run unit tests automatically
main(module='arithmetic_test', exit=False)