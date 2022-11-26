package main

import "fmt"

// halve the input, rounded down,
// never reaching 0, e.g.:
//   5
// returns:
//   2
func halve(x int) int {
	v := x / 2
	if v < 1 {
		v = 1
	}

	return v
}

func main() {
	fmt.Printf("%d\n", halve(5))
}
