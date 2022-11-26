package main

import "fmt"

// return a list of n numbers
// with values from 2 to n+1
// e.g
//   explode(10)
// returns:
//   [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
func explode(n int) []int {
	r := []int{}
	for i := 2; i <= n+1; i++ {
		r = append(r, i)
	}

	return r
}

func main() {
	fmt.Printf("%v\n", explode(11))
}
