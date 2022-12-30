package main

import "fmt"

// increment the input, e.g.:
//   5
// returns:
//   6
func increment(x int) int {
	v := x + 1
	return v
}

func main() {
	fmt.Printf("%d\n", increment(5))
}
