package Day8;

class MyLinkedList {

    private ListNode head;
    private ListNode tail;
    private int size;

    /** Initialize your data structure here. */

    public MyLinkedList() {
        this.head = this.tail = null;
        this.size = 0;
    }

    /** Get the value of the index-th node in the linked list. If the index is invalid, return -1. */
    public int get(int index) {
        int i=0;
        ListNode current=this.head;
        while (i<=index){
            if(i==index){
                return current.val;
            }
            i++;
            current=current.next;
        }
        return  current.val;
    }

    /** Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list. */
    public void addAtHead(int val) {
    if(this.size==0){
        this.head=new ListNode(val);
        this.tail=this.head;
        this.size++;
    }
    else{
        ListNode temp=this.head;
        this.head=new ListNode(val);
        this.head.next=temp;
        this.size++;
    }
    }

    /** Append a node of value val to the last element of the linked list. */
    public void addAtTail(int val) {
        ListNode n = new ListNode(val);
        if (this.size == 0)
        {
            this.head = this.tail = n;
            this.size++;}
        else{
            this.tail = this.tail.next = n;
        }


    }

    /** Add a node of value val before the index-th node in the linked list. If index equals to the length of linked list, the node will be appended to the end of linked list. If index is greater than the length, the node will not be inserted. */
    public void addAtIndex(int index, int val) {
        if (index < 0 || index > this.size) return;
        if (index == 0)  { this.addAtHead(val); return; }
        if (index == size) { this.addAtTail(val); return; }
        ListNode prev = this.getAt(index - 1);
        ListNode temp= prev.next;
        prev.next = new ListNode(val);
        (prev.next).next=temp;
        ++this.size;
    }

    public ListNode getAt(int i) {
        int j=0;
        ListNode current=this.head;
        while (j<=i){
            if(j==i){
                return current;
            }
            current=current.next;
            j++;
        }
        return current;
    }

    /** Delete the index-th node in the linked list, if the index is valid. */
    public void deleteAtIndex(int index) {
        if (index < 0 || index >= this.size) return;
        ListNode prev = this.getAt(index - 1);
        prev.next = prev.next.next;
        if (index == 0) this.head = prev.next;
        if (index == this.size - 1) this.tail = prev;
        --this.size;
    }
}

/**
 * Your MyLinkedList object will be instantiated and called as such:
 * MyLinkedList obj = new MyLinkedList();
 * int param_1 = obj.get(index);
 * obj.addAtHead(val);
 * obj.addAtTail(val);
 * obj.addAtIndex(index,val);
 * obj.deleteAtIndex(index);
 */