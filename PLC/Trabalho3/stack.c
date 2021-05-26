#include <stdio.h>
#include <stdlib.h>
#define MAXSIZE 100
 
struct STACK
{
    int stk[MAXSIZE];
    int sp;
};
typedef struct STACK* stack; 

int top(stack s){
    int elem;
    if (s->sp > -1)
    {
        elem = s->stk[s->sp];
    }
    return elem;
}

void push (stack s, int elem) {
    if (s->sp < MAXSIZE){
	    s->sp++;
	    s->stk[s->sp] = elem;
	}
}

int pop (stack s) {
    int elem;
    if (s->sp > -1)
    {
        elem = s->stk[s->sp];
        s->sp--;
    }
    return elem;
}

stack initStack (){
	stack s = (struct STACK*)malloc(sizeof(struct STACK));
	s->sp=-1;
	return s;