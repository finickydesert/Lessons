//a quick summary of notes for this
/*
go tools
-go build: compiles the program, arguments can be a list of .go files or packages. it creates a executable in the same name as the .go file
-go doc: prints documentation for a package
-go fmt: format source code files
-go get: downloads packages and installs them
-go list: list all the installed packages
-go run compiles .go files and runs the executable
-Go test: it runs tests.
*/
/*varibles
case sensitive can use numbers
must have name, type, and declerations
you can can declare many on the same line seperated by comma
type declerations may improve clarity and define a alias
ex:
type Celsius float64
type IDum int
you can declare variables using type alias
ex:
var temp Celsius
var pid IDnum
*/
/*
== initializing
either var x in = 100 or var x = 100
specify type may eliminate future problems
uninitalized variables have 0 value
ex:
var x int
var x string
-short var declerations :=
ex
x := 100
can only do inside a function
*/

package main
import "fmt"
func main() {
  fmt.Printf("Hello, World")
  fmt.Printf("a quick summary of notes for this week") 
  fmt.Printf("go tools")
  fmt.Printf("go build: compiles the program, arguments can be a list of .go files or packages. it creates a executable in the same name as the .go file")
  fmt.Printf("go doc: prints documentation for a package")
  fmt.Printf("go fmt: format source code files")
  fmt.Printf("go get: downloads packages and installs them")
  fmt.Printf("go list: list all the installed packages")
  fmt.Printf("go run compiles .go files and runs the executable")
  fmt.Printf("Go test: it runs tests.")
  fmt.Printf("*******") 
  fmt.Printf("case sensitive can use numbers")
  fmt.Printf("must have name, type, and declerations")
  fmt.Printf("you can can declare many on the same line seperated by comma")
  fmt.Printf("type declerations may improve clarity and define a alias")
  fmt.Printf("ex: ")
  fmt.Printf("type Celsius float64")
  fmt.Printf("type IDum int")
  fmt.Printf("you can declare variables using type alias")
  fmt.Printf("ex: ")
  fmt.Printf("var temp Celsius")
  fmt.Printf("var pid IDnum")
  fmt.Printf("== initializing")
  fmt.Printf("either var x in = 100 or var x = 100")
  fmt.Printf("specify type may eliminate future problems")
  fmt.Printf("uninitalized variables have 0 value")
  fmt.Printf("ex:")
  fmt.Printf("var x int")
  fmt.Printf("var x string")
  fmt.Printf("-short var declerations :=")
  fmt.Printf("ex")
  fmt.Printf("x := 100")
  fmt.Printf("can only do inside a function")
           
}
