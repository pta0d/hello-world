#include <stdio.h>

int a, b, s;

int main() {
  printf("Enter 2 integers separated by space: ");
  scanf("%d %d", &a, &b);
  s = a + b;
  printf("Sum a + b = %d\n", s);

  //getch();
  return 0;
}