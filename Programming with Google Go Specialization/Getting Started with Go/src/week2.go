/* Notes
pointers:
a pointer is a address to data in memory
2 operators &, *
the & operator returns the address of a function or var
the * operator returns the data at am address
opposites of each other
alternate way to create a var is by using the new() function. new() creates amd returns a pointer to a variable.
buy default variable is initalized to zero.
*/
/*
Variable Scope:
the places in the code where a var can be accesed
Blocks are used for var scoping in go
a sequence of declerations and statements within matching {} (brakets)
-including function deffinitions
hierarchy of implicit blocks
universal block: all go source
package block: all source in a package
file block: all source in a file
if, for switch statement
clauses that are in switch or select
*/
/*
lexical scoping
watch the vid for a majority of explanation
*/
/*
Deallocating Memory
when var is not needed then it should be deallocated
memeroy space will be available because of this
stack vs heap:
stack is within the function is local and deals with local var it'll deallocate after the function compleates
heap is outside the function and is global heap is persistant
data on heap must be deallocated when done being used.
ex:
x = mark(32);
free(x)
error prone, but fast.
*/
