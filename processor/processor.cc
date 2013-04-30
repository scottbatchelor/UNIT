#include <iostream>
#include <fstream>
#include <string>
#include <unistd.h>

int main(int argc, char** argv)
{
  std::ifstream in(argv[1]);
  std::string uuid(argv[2]);
  do
  {
    std::string l;
    std::getline(in, l);
    std::cout << "[" << uuid << "] " << l << std::endl;
    sleep(1);
  } while (!in.eof());

  return 0;
}


