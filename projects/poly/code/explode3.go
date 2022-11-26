package main

import "fmt"

// return a list of n times
// the number n + 1
// e.g
//   explode(5)
// returns:
//   [6, 6, 6, 6, 6]
func explode(n int) []int {
	r := []int{}
	for i := 0; i < n; i++ {
		r = append(r, n+1)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", explode(11))
}
