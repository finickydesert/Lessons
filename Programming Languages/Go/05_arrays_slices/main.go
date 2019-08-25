package main

import "fmt"

func main() {
	// Arrays 
	//var fruitArr [2]string
	// // assigned values
	//fruitArr[0] = "apple"
	//fruitArr[1] = "orange"
	//fmt.Println(fruitArr)
	//fruitArr:= [2]string{"apple", "orange"}
	//fmt.Println(fruitArr[1])
	//fmt.Println(fruitArr)
	fruitSlice:= []string{"apple", "orange", "grape", "cherry"}
	fmt.Println(fruitSlice)
	fmt.Println(len(fruitSlice))
	fmt.Println(fruitSlice[1:3])
}
