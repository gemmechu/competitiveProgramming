package Day8;

import java.util.ArrayList;

public class ReverseLinkedList {

    public  static void main(String[] args){
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(2);
        ListNode c = new ListNode(3);
        ListNode d = new ListNode(4);
        ListNode e = new ListNode(5);
        a.next=b;
        b.next=c;
        c.next=d;
        d.next=e;
        ListNode reversed= new ListNode(a.val);
        MyLinkedList myLinkedList = new MyLinkedList();
        myLinkedList.addAtHead(4);
        myLinkedList.addAtTail(0);
        myLinkedList.addAtHead(7);
        myLinkedList.addAtHead(9);
        myLinkedList.addAtIndex(1,8);
        myLinkedList.deleteAtIndex(0);
        System.out.println(myLinkedList.getAt(0).val);
        System.out.println(myLinkedList.getAt(1).val);
        System.out.println(myLinkedList.getAt(2).val);


        ReverseLinkedList myclass = new ReverseLinkedList();

        //ListNode reversList = myclass.reverseListMethod(b);

    }
    public ListNode reverseListMethod(ListNode head) {
        ListNode temp;
        ListNode reversed = new ListNode(head.val);
        reversed.next=null;
        head=head.next;

        while (true){
            temp= head.next;
            head.next=reversed;
            reversed= head;
            if(temp == null){
                break;
            }
            head=temp;


        }
        return reversed;

    }
}



