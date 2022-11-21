package main

import "fmt"

func avg(x []int) float32 {
	sum := float32(0)

	for _, v := range x {
		sum += float32(v)
	}

	return sum / float32(len(x))
}

func main() {
	fmt.Printf("%v", avg([]int{1, 2, 1, 1, 1, 3, 1}))
}
