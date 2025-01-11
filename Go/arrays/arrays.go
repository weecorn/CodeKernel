package main

import (
	"fmt"
)

type Array struct {
	data     []int // Slice to hold the array elements
	size     int   // Current number of elements
	capacity int   // Maximum capacity of the array
}

// Initialize a new array with a given capacity
func NewArray(capacity int) *Array {
	return &Array{
		data:     make([]int, capacity),
		size:     0,
		capacity: capacity,
	}
}

// Insert an element into the array
func (arr *Array) Insert(element int) {
	if arr.size >= arr.capacity {
		fmt.Println("Array is full! Cannot insert element.")
		return
	}
	arr.data[arr.size] = element
	arr.size++
}

// Delete an element at a specific index
func (arr *Array) Delete(index int) {
	if index < 0 || index >= arr.size {
		fmt.Println("Invalid index!")
		return
	}
	for i := index; i < arr.size-1; i++ {
		arr.data[i] = arr.data[i+1]
	}
	arr.data[arr.size-1] = 0 // Clear the last element
	arr.size--
}

// Display the array contents
func (arr *Array) Display() {
	if arr.size == 0 {
		fmt.Println("Array is empty!")
		return
	}
	fmt.Print("Array elements: ")
	for i := 0; i < arr.size; i++ {
		fmt.Print(arr.data[i], " ")
	}
	fmt.Println()
}

func main() {
	// Initialize an array with a capacity of 10
	arr := NewArray(10)

	// Insert elements into the array
	arr.Insert(5)
	arr.Insert(10)
	arr.Insert(15)

	// Display the array contents
	arr.Display()

	// Delete an element at index 1
	arr.Delete(1)

	// Display the array contents again
	arr.Display()
}
