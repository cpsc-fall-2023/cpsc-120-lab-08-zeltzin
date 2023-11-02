// Zeltzin Martinez Rodriguez
// martinez.zeltzin408@csu.fullerton.edu
// @zeltzin-mtz
// Partners: @none

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments{argv, argv + argc};
  if (arguments.size() != 4) {
    std::cerr << "Please enter 3 arguments \n";
    return 1;
  }
  std::string protein;
  std::string bread;
  std::string condiment;
  protein = arguments[1];
  bread = arguments[2];
  condiment = arguments[3];
  std::cout << "A " << protein << " sandwich on " << bread << " with "
            << condiment;
  return 0;
}
