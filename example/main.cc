#include <cstdio>

extern "C" float fadd(float x, float y);

int main(int argc, char** argv)
{
  float val = fadd(static_cast<float>(argc), 2.4f);
  printf("val = %f\n", val);
  (void)argv;
  return 0;
}
