glossary = {"print":"Is a function which prints a specified message to the screen",
            "variable":"reserved memory location to store values", 
            "list":"data structure in Python that is a mutable, or changeable, ordered sequence of elements", 
            "conditional statements":"used to handle conditions in your program", 
            "integer":"is a whole number, positive or negative, without decimals, of unlimited length.",
            "float":"a method that returns a floating-point number for a provided number or string",
            "pop":"removes the specified item from the dictionary",
            "loop":"repeating something over and over until a particular condition is satisfied.",
            "string":"a collection of alphabets, words or other characters",
            "boolean":"used to represent the truth value of an expression."}

for key, definition in glossary.items():
    print("\n" + key.title() + ": " + definition)