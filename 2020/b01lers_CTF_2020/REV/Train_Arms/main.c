#include <stdio.h>

char flag[29] = "REDACTED"; // len = 28

int main(void)
{
  int i=0;
  while(flag[i] != "\0") {
    if(i % 2 == 1) { // if odd
      flag[i] = flag[i] ^ 42;
    } else {
      flag[i] = flag[i];
    }
    i++;
  }
  return 0;
}
