package day7;

import java.util.LinkedList;
import java.util.Queue;

public class MyStack {
    static Queue<Integer> q1 = new LinkedList<Integer>();
    static Queue<Integer> q2 = new LinkedList<Integer>();
    static int curr_size;
    /** Initialize your data structure here. */
    public MyStack() {
    curr_size=0;
    }

    /** Push element x onto stack. */
    public void push(int x) {
        curr_size++;


        q2.add(x);

        while (!q1.isEmpty()) {
            q2.add(q1.peek());
            q1.remove();
        }


        Queue<Integer> q = q1;
        q1 = q2;
        q2 = q;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {

        if (q1.isEmpty())
            return
        curr_size--;
        return q1.remove();
    }

    /** Get the top element. */
    public int top() {
        if (q1.isEmpty())
            return -1;
        return q1.peek();
    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
               return q1.isEmpty() & q2.isEmpty();
    }
}
