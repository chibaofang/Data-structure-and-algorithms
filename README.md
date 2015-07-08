# Data-structure-and-algorithms
This repository store the source codes for baisic data strutures and algorithms. Most of them are written by myself, while some of them are excellent code (modified) from the internet. What is certain is that they are right.

##Data Structure

###linked_list

###queue

###stack
```
/* a stack interface model*/

#define STACK_TYPE int

void push(STACK_TYPE value);  /*push*/
void pop(STACK_TYPE value);   /*pop*/
STACK_TYPE top(void);
int is_empty(void);
int is_full();
```
```
#include "stack.h"
#include<assert.h>

#define STACK_SIZE 100

static STACK_TYPE stack[STACK_SIZE];
static int top_element = -1;

push(STACK_TYPE value){
  assert(!is_full());
  top_element += 1;
  stack[top_element] = value;
}

pop(void){
  asser(!is_empty());
  top_element -= 1;
}

STACK_TYPE top(void){
  assert(!is_empty());
  return stack[top_element];
}

int is_empty(void){
  return top_element == -1;
}

int is_full(void){
  return top_element ==STACK_SIZE - 1;
}
```
###tree
```
/*tree traversal*/
void inorder(tree_pointer ptr)
{
  if (ptr){
    inorder(ptr->left_child);
    printf("%d",ptr_data);
    inorder(ptr->right_child);
  }
}

void preorder(tree_pointer ptr)
{
  if(ptr){
    printf("%d",ptr_data);
    inorder(ptr->left_child);
    inorder(ptr->right_child);
  }
}

void postorder(tree_pointer ptr)
{
  if(ptr){
    inorder(ptr->left_child);
    inorder(ptr->right_child);
     printf("%d",ptr_data);
  }
}


/*copy a binary tree*/
tree_pointer copy(tree_pointer original) {
  tree_pointer temp;
  if(original) {
    temp = (tree_pointer) malloc(sizeof(node));
    if(IS_FULL(temp)) {
      fprintf(stderr, "The memory is full\n");
      exit(1);
    }
    temp->left_child = copy(original->left_child);
    temp->right_child = copy(original->right_child);
    temp->data = original->data;
    return temp;
  }
  return NULL;
}


/*equal or not*/
int equal(tree_pointer first, tree_pointer second) {
  return (!first && !second)||(first && second && (first->data == second->data) && equal(first->left_child, second_child) && (equal(first->right_child, second->right_child))) 
}
```

###graph



##Algorithms

