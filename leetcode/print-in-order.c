#include <stdlib.h>
#include <unistd.h>

void printFirst();
void printSecond();
void printThird();

typedef struct {
    volatile int round;
} Foo;

Foo* fooCreate() {
    Foo* obj = (Foo*) malloc(sizeof(Foo));
    obj->round = 1;
    return obj;
}
void incr(Foo* obj) {
    obj->round = obj->round + 1;
}

void sleep_(Foo* obj, int round) {
    while(obj->round != round) {
        sleep(0);
    }
}

void first(Foo* obj) {
    printFirst();
    incr(obj);
}

void second(Foo* obj) {
    sleep_(obj, 2);
    printSecond();
    incr(obj);
}

void third(Foo* obj) {
    sleep_(obj, 3);
    printThird();
}

void fooFree(Foo* obj) {
    free(obj);
}
