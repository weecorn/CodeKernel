#include <stdio.h>
#include <stdlib.h>

// Define a structure for the stack
typedef struct {
    int *data;    // Pointer to the stack elements
    int top;      // Index of the top element
    int capacity; // Maximum capacity of the stack
} Stack;

// Function to initialize the stack
Stack* initializeStack(int capacity) {
    Stack *stack = (Stack*)malloc(sizeof(Stack));
    stack->data = (int*)malloc(capacity * sizeof(int));
    stack->top = -1;
    stack->capacity = capacity;
    return stack;
}

// Function to check if the stack is empty
int isEmpty(Stack *stack) {
    return stack->top == -1;
}

// Function to check if the stack is full
int isFull(Stack *stack) {
    return stack->top == stack->capacity - 1;
}

// Function to push an element onto the stack
void push(Stack *stack, int element) {
    if (isFull(stack)) {
        printf("Stack overflow! Cannot push %d onto the stack.\n", element);
        return;
    }
    stack->data[++stack->top] = element;
}

// Function to pop an element from the stack
int pop(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack underflow! Cannot pop from an empty stack.\n");
        return -1; // Return a sentinel value to indicate failure
    }
    return stack->data[stack->top--];
}

// Function to peek at the top element of the stack
int peek(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty! Cannot peek.\n");
        return -1; // Return a sentinel value to indicate failure
    }
    return stack->data[stack->top];
}

// Function to display the stack contents
void displayStack(Stack *stack) {
    if (isEmpty(stack)) {
        printf("Stack is empty!\n");
        return;
    }
    printf("Stack elements: ");
    for (int i = 0; i <= stack->top; i++) {
        printf("%d ", stack->data[i]);
    }
    printf("\n");
}

// Function to free the memory used by the stack
void freeStack(Stack *stack) {
    free(stack->data);
    free(stack);
}

int main() {
    // Initialize a stack with a capacity of 5
    Stack *stack = initializeStack(5);

    // Push elements onto the stack
    push(stack, 10);
    push(stack, 20);
    push(stack, 30);

    // Display the stack contents
    displayStack(stack);

    // Peek at the top element
    printf("Top element: %d\n", peek(stack));

    // Pop an element from the stack
    printf("Popped element: %d\n", pop(stack));

    // Display the stack contents again
    displayStack(stack);

    // Free the allocated memory
    freeStack(stack);

    return 0;
}
