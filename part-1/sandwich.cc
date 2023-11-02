// Zeltzin Martinez Rodriguez
// martinez.zeltzin408@csu.fullerton.edu
// @zeltzin-mtz
// Partners: @none

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments{argv, argv + argc};
  if (argc != 3) {
    std::cerr << "Please enter 3 arguments";
    return 1;
  }
  // TODO: Validate that the number of arguments is correct.
  // If not, print an error message and return a non-zero value.
  std::string protein;
  std::string bread;
  std::string condiment;
  protein = arguments[1];
  bread = arguments[2];
  condiment = arguments[3];
  // TODO: Declare three std::string variables to hold the
  // protein, bread, and condiment input.
  // Initialize each variable with an element of the arguments vector
  // declared above.
  std::cout << "A " << protein << "sandwich on " << bread << "with "
            << condiment;
  // TODO: Use cout to print output following the pattern
  // Your order: A *PROTEIN* sandwich on *BREAD* with *CONDIMENT*.
  // on its own line.

  return 0;
}
