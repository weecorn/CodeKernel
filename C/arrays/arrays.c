#include <stdio.h>
#include <stdlib.h>

// Define a structure for the array
typedef struct {
    int *data;    // Pointer to the array data
    int size;     // Current number of elements in the array
    int capacity; // Maximum capacity of the array
} Array;

// Function to initialize the array
Array* initializeArray(int capacity) {
    Array *arr = (Array*)malloc(sizeof(Array));
    arr->data = (int*)malloc(capacity * sizeof(int));
    arr->size = 0;
    arr->capacity = capacity;
    return arr;
}

// Function to insert an element into the array
void insertElement(Array *arr, int element) {
    if (arr->size >= arr->capacity) {
        printf("Array is full! Cannot insert element.\n");
        return;
    }
    arr->data[arr->size] = element;
    arr->size++;
}

// Function to delete an element at a specific index
void deleteElement(Array *arr, int index) {
    if (index < 0 || index >= arr->size) {
        printf("Invalid index!\n");
        return;
    }
    for (int i = index; i < arr->size - 1; i++) {
        arr->data[i] = arr->data[i + 1];
    }
    arr->size--;
}

// Function to display the array contents
void displayArray(Array *arr) {
    if (arr->size == 0) {
        printf("Array is empty!\n");
        return;
    }
    printf("Array elements: ");
    for (int i = 0; i < arr->size; i++) {
        printf("%d ", arr->data[i]);
    }
    printf("\n");
}

// Function to free the memory used by the array
void freeArray(Array *arr) {
    free(arr->data);
    free(arr);
}

int main() {
    // Initialize an array with a capacity of 10
    Array *arr = initializeArray(10);

    // Insert elements into the array
    insertElement(arr, 5);
    insertElement(arr, 10);
    insertElement(arr, 15);

    // Display the array contents
    displayArray(arr);

    // Delete an element at index 1
    deleteElement(arr, 1);

    // Display the array contents again
    displayArray(arr);

    // Free the allocated memory
    freeArray(arr);

    return 0;
}
