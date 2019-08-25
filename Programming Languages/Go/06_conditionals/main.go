package main

import "fmt"

func main() {
	x:= 15
	y:= 10

	//if else
	if x<y{
		fmt.Printf("%d is less than %d\n", x, y)
	} else {
		fmt.Printf("%d is less than %d\n", y, x)

	}
//else if
color := "red"
if color == "red"{
	fmt.Printf("the color is red\n")
} else if color == "blue"{
	fmt.Printf("color is not blue ot red")
}
// switch
switch color {
case "red":
	fmt.Println("color is red")
case "blue":
	fmt.Println("color is blue")
default:
	fmt.Println("color is not blue or red")
}
}