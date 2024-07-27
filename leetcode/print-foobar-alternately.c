#include <stdbool.h>
#include <stdlib.h>
#include <unistd.h>

void printFoo();
void printBar();

typedef struct {
    int n;
    volatile bool turn;
} FooBar;

FooBar* fooBarCreate(int n) {
    FooBar* obj = (FooBar*) malloc(sizeof(FooBar));
    obj->n = n;
    obj->turn = false;
    return obj;
}

void foo(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        while (obj->turn) {
            sleep(0);
        }
        printFoo();
        obj->turn = true;
    }
}

void bar(FooBar* obj) {
    for (int i = 0; i < obj->n; i++) {
        while (!(obj->turn)) {
            sleep(0);
        }
        printBar();
        obj->turn = false;
    }
}

void fooBarFree(FooBar* obj) {
    free(obj);
}
