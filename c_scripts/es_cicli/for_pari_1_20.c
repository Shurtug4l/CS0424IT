#include <stdio.h>

int main() {
  // Ciclo for per stampare i numeri pari da 1 a 20
  for (int i = 1; i <= 20; i++) {
    if (i % 2 == 0) {
      printf("%d\n", i);
    }
  }

  return 0;
}
