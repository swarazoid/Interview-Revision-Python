"""
Use case:
The Interpreter Design Pattern is used to evaluate or process a language or expression by defining a grammar and providing an interpreter for it. Below is an example of solving mathematical expressions using the Interpreter pattern.

Basically it feels like composite + context
"""

from abc import ABC, abstractmethod

# Abstract Expression
class Expression(ABC):
    @abstractmethod
    def interpret(self):
        pass


# Terminal Expressions
class Number(Expression):
    def __init__(self, value):
        self.value = value

    def interpret(self):
        return self.value


class Add(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() + self.right.interpret()


class Subtract(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() - self.right.interpret()


class Multiply(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() * self.right.interpret()


class Divide(Expression):
    def __init__(self, left: Expression, right: Expression):
        self.left = left
        self.right = right

    def interpret(self):
        return self.left.interpret() // self.right.interpret()  # Integer division


# Context for parsing expressions
class ExpressionParser:
    @staticmethod
    def parse(expression: str):
        """Parses a simple mathematical expression into an abstract syntax tree."""
        stack = []
        tokens = expression.split()

        for token in tokens:
            if token.isdigit():
                stack.append(Number(int(token)))
            elif token == "+":
                right = stack.pop()
                left = stack.pop()
                stack.append(Add(left, right))
            elif token == "-":
                right = stack.pop()
                left = stack.pop()
                stack.append(Subtract(left, right))
            elif token == "*":
                right = stack.pop()
                left = stack.pop()
                stack.append(Multiply(left, right))
            elif token == "/":
                right = stack.pop()
                left = stack.pop()
                stack.append(Divide(left, right))
            else:
                raise ValueError(f"Unknown token: {token}")

        return stack.pop()


# Example Usage
if __name__ == "__main__":
    expression = "5 3 + 8 * 2 /"  # (5 + 3) * 8 / 2 = 32
    tree = ExpressionParser.parse(expression)
    result = tree.interpret()
    print(f"The result of the expression '{expression}' is: {result}")


"""
When to Use the Interpreter Pattern?
The Interpreter Pattern is most useful when:

Domain-Specific Language (DSL): You have a well-defined grammar for a small language or expression, such as mathematical expressions, configuration files, or queries.
Repeated Use of Grammar: The grammar will be used frequently, and a reusable and extendable interpreter is beneficial.
Simple Syntax and Small Problem Domain: The language or syntax is small and not overly complex.

Is the Interpreter Pattern Similar to the Composite Pattern?
Yes, the Interpreter Pattern shares similarities with the Composite Pattern in the following ways:

Similarities

Tree Structure:
Both patterns often use a tree-like structure to represent expressions or hierarchical data.
For example, in the Interpreter Pattern, a mathematical expression is parsed into an abstract syntax tree.

Recursive Processing:
Both patterns rely on recursive processing. In the Interpreter Pattern, interpreting an expression involves recursively interpreting its components. Similarly, in the Composite Pattern, operations are applied recursively on composite elements.

Common Base Class:
Both patterns define a base class or interface (e.g., Component in Composite, Expression in Interpreter) to ensure consistent behavior across components or expressions.

Differences

Aspect	    -Interpreter Pattern	                                                        -Composite Pattern
Focus	    -Solving problems related to language parsing or evaluating expressions.	    -Representing hierarchical structures of objects where leaf and composite objects share the same interface.
Use Case	-Evaluating expressions, queries, or DSLs.	                                    -Modeling part-whole hierarchies, such as files and folders, or GUI components.
Behavior	-Focuses on interpreting or executing based on grammar rules.	                -Focuses on uniformly treating individual and composite objects.
Structure	-Expression trees for recursive evaluation.	                                    -General trees for organizing and operating on nested components.
"""