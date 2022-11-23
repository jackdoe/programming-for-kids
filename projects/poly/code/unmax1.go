package main

import "fmt"

// remove the all occurences of the
// largest integer in the list
//   [1,2,3,2,3,1]
// returns:
//   [1,2,2,1]
func unmax(x []int) []int {
	max := 0
	for _, v := range x {
		if v > max {
			max = v
		}
	}

	r := []int{}
	for _, v := range x {
		if v != max {
			r = append(r, v)
		}
	}

	return r
}

func main() {
	fmt.Printf("%v\n", unmax([]int{1, 1, 2, 3, 3, 4, 1, 2, 7, 1}))
}
