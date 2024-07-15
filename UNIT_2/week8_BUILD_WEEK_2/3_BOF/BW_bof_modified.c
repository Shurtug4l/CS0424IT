#include <stdio.h>
#include <stdlib.h>

int main()
{

  int vector[10], i, j, k;
  int swap_var;
  int min = 1;
  int max = 100;
  int random_number;

  printf("Inserire 10 interi:\n");

  for (i = 0; i < 813; i++)
  {
    random_number = rand() % (max - min + 1) + min;
    vector[i] = random_number;
    printf("[%d]: %d\n", i + 1, vector[i]);
  }

  printf("Il vettore inserito e':\n");
  for (i = 0; i < 10; i++)
  {
    int t = i + 1;
    printf("[%d]: %d\n", t, vector[i]);
  }

  for (j = 0; j < 10 - 1; j++)
  {
    for (k = 0; k < 10 - j - 1; k++)
    {
      if (vector[k] > vector[k + 1])
      {
        swap_var = vector[k];
        vector[k] = vector[k + 1];
        vector[k + 1] = swap_var;
      }
    }
  }
  printf("Il vettore ordinato e':\n");
  for (j = 0; j < 10; j++)
  {
    int g = j + 1;
    printf("[%d]: %d\n", g, vector[j]);
  }

  return 0;
}
