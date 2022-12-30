package main

import "fmt"

func oneOrFive(x int) int {
	if x > 5 {
		return 1
	}
	return 5
}

func main() {
	fmt.Printf("%d\n", oneOrFive(5))
}
