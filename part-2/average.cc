// Zeltzin Martinez Rodriguez
// martinez.zeltzin408@csu.fullerton.edu
// @zeltzin-mtz
// Partners: @none

#include <iostream>
#include <string>
#include <vector>

int main(int argc, char* argv[]) {
  std::vector<std::string> arguments{argv, argv + argc};
  if (arguments.empty()) {
    std::cout << "Please enter 1 value";
    return 1;
  }
  double sum = 0.0;
  for (int i = 0; i < arguments.size(); i++) {
    double number = std::stod(argv[i]);
    sum += number;
  }
  double average = sum / arguments.size();
  std::cout << "Average = " << average;
  return 0;
}
