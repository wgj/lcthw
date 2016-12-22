#include <stdio.h>
#define LENGTH 255


void push(int stack[], int item){
  // shift stack[i] to stack[i+1]
  // if stack is empty
  for (i = 0; i < LENGTH; i++) {
    // copy i+1
    // move i to i+1
  }
  // insert item into stack[0]
}

int pop(int stack[]){
  // Return the 0th item in stack.
  // Shift stack[i] to stack[i-1]
  return 0;
}

int main(int argc, char *argv[])
{
  int stack[LENGTH];
  push(stack, 1);
  push(stack, 2);
  printf("pop(stack): %d", pop(stack));
  printf("pop(stack): %d", pop(stack));
  return 0;
}
