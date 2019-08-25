package main

import "fmt"

func main() {
	// long method
	i:= 1
	for i<= 10{
	fmt.Println(i)
	i ++
	}
// short
for i := 1; i <= 10; i++ {
	fmt.Printf("Number %d\n", i)
}

//fizzbuzz
for i := 1; i <= 100; i++ {
	if 1%15 == 0 {
		fmt.Println("fizzbuzz")
	} else if i%3 == 0 {
		fmt.Println("fizz")
	} else if i%5 == 0 {
		fmt.Println("buzz")
	} else {
		fmt.Println(i)
	}
	}
}