# 4917 Assembler

## Introduction

Next to running 4917 programs in matrix format, the simulator can also run programs written in 4917 mini assembly language as described in this document.

## Language Definition

### Line Formats

#### Comment Line

```text
; This is a comment line
```

#### Stand-alone Label

```text
label: [;comment]
```

#### Instruction

```text
[label:] mnemonic [operands] [;comment]
```

White space is ignored.

### Instruction Set

<!-- prettier-ignore -->
opcode | mnemonic | operand(s) | description
:-----:|----------|---------|------------
0 | HLT | | Print `*** HALT ***` and stop execution
1 | ADD | | R0 = R0 + R1
2 | SUB | | R0 = R0 - R1
3 | INC | R0 | Increment R0
4 | INC | R1 | Increment R1
5 | DEC | R0 | Decrement R0
6 | DEC | R1 | Decrement R1
7 | BEEP | | Print `*** BEEP ***`
8 | PRINT | number | Print `*** <number> ***`
9 | LD | R0,X | Load the value of address X into R0
10 | LD | R1,X | Load the value of address X into R1
11 | ST | R0,X | Store the value of R0 into address X
12 | ST | R1,X | Store the value of R1 into address X
13 | B | X | Jump to location X
14 | BZ | X | Jump to X if R0 is equal to 0
15 | BNZ | X | Jump to X if R0 is **not** equal to 0

The value of X can be one of the following:

- A number in the range of 0 <= X < 16, for example

  ```text
  LD R0,5  ;Load the memory cell at address 5
  ```

- A label, for example:

  ```text
  LD R0,count  ;Load the memory cell at the location of label <count>
  ...
  count:
    .data 4
  ```

- A label with positive of negative offset, for example:

  ```text
  LD R0,count+1  ;Load the memory cell at the location of label <count> + 1
  ...
  count:
    .data 4
    .data 5
  ```
