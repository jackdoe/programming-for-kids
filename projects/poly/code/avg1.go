package main

import "fmt"

func avg(x []int) int {
	sum := 0

	for _, v := range x {
		sum += v
	}

	return sum / len(x)
}

func main() {
	fmt.Printf("%v", avg([]int{1, 2, 1, 1, 1, 3, 1}))
}
