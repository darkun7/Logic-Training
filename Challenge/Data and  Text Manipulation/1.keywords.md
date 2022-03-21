# Case: Keywords
Create program that will able to create array of keywords that can be used as search engine
## Inputs
 - example 1:
 getKeyWord("clean white paper")
 - example 2:
 getKeyWord("clean white blank paper")
## Outputs
 - example 1:
```
[
    'clean white paper',
    'clean white', 
    'clean', 
    'white paper', 
    'white', 
    'paper'
]
```
 - example 2:
```
[
    'clean white blank paper', 
    'clean white blank', 
    'clean white', 
    'clean', 
    'white blank paper', 
    'white blank', 
    'white', 
    'blank paper', 
    'paper', 
    'blank'
]
```