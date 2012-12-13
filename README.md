The use of double-head queue
=============================
* * *
Use the double-head queue of numbers of type int. Double-head queue allows to put members at the beginning and at the end of the queue as well.

Code example:

    class DBL_Queue {
        // write your variables and methods here
    };
    
**Inside DBL_Queue the following functions should be used**

1. DBL_Queue() - constuctor of the queue
2. DBL_Queue~() - destructor for the queue - deletes the queue and cleans the memory which it took
3. const int get_queue_size() - return the number of members in the queue
4. void enqueueBeg(int) - add a member to the head of the queue
5. int dequeueBeg() - remove a member from the head and return it
6. void enqueueEnd(int) - add a member to the tail of the queue
7. int dequeueEnd() - remove a member from the tail of the queue and return it
8. void concatQueue(const DBL_Queue* otherQ) - adds otherQ to the tail of the calling queue
9. void printQueue() - prints the queue

Example output
---------------
* 789 17 4 7; queue size: 4 
* 221 8 3 864; queue size: 4 
* 221 8 3 864 789 17 4 7; queue size: 8 
* 8 3 864 789 17 4 7; queue size: 7 

Functions 2 and 9 should perform with complexity of O(n).
Functions 1,3,4,5,6,7,8 - O(1).