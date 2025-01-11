package main

import (
	"fmt"
)

// Stack structure
type Stack struct {
	elements []int
}

// Push adds an element to the top of the stack
func (s *Stack) Push(value int) {
	s.elements = append(s.elements, value)
	fmt.Printf("%d pushed onto the stack.\n", value)
}

// Pop removes and returns the top element of the stack
func (s *Stack) Pop() int {
	if s.IsEmpty() {
		fmt.Println("Stack underflow! Cannot pop.")
		return -1 // Sentinel value for underflow
	}
	// Get the top element
	top := s.elements[len(s.elements)-1]
	// Remove the top element
	s.elements = s.elements[:len(s.elements)-1]
	return top
}

// Peek returns the top element without removing it
func (s *Stack) Peek() int {
	if s.IsEmpty() {
		fmt.Println("Stack is empty! Cannot peek.")
		return -1 // Sentinel value for empty stack
	}
	return s.elements[len(s.elements)-1]
}

// IsEmpty checks if the stack is empty
func (s *Stack) IsEmpty() bool {
	return len(s.elements) == 0
}

// Display prints the current stack
func (s *Stack) Display() {
	fmt.Println("Stack:", s.elements)
}

func main() {
	// Create a new stack
	var stack Stack

	// Push elements onto the stack
	stack.Push(10)
	stack.Push(20)
	stack.Push(30)

	// Display the stack
	stack.Display()

	// Peek the top element
	fmt.Printf("Top element: %d\n", stack.Peek())

	// Pop elements from the stack
	fmt.Printf("Popped: %d\n", stack.Pop())
	fmt.Printf("Popped: %d\n", stack.Pop())

	// Peek after popping
	fmt.Printf("Top element: %d\n", stack.Peek())

	// Pop remaining elements
	fmt.Printf("Popped: %d\n", stack.Pop())
	fmt.Printf("Popped: %d\n", stack.Pop()) // Should show underflow
}
