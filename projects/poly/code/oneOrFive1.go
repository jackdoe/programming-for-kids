package main

import "fmt"

// return 1 if the number is bigger than 5
// return 5 if otherwise, e.g.:
//   3
// returns:
//   5
func oneOrFive(x int) int {
	if x > 5 {
		return 1
	}
	return 5
}

func main() {
	fmt.Printf("%d\n", oneOrFive(5))
}
