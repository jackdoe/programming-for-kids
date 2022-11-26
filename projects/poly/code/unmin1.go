package main

import "fmt"

// remove the all occurences of the
// smallest integer in the list
//   [1,2,3,2,3,1]
// returns:
//   [2,3,2,3]
func unmin(x []int) []int {
	min := 2147483647
	for _, v := range x {
		if v < min {
			min = v
		}
	}

	r := []int{}
	for _, v := range x {
		if v != min {
			r = append(r, v)
		}
	}

	return r
}

func main() {
	fmt.Printf("%v\n", unmin([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
