
public class AddTwoNumber {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        int sum = 0;
        int carry = 0;
        ListNode currentNode = new ListNode(0);
        ListNode currentNodeHead = currentNode;
        while(l1!=null || l2!=null){
            int a = l1!=null ? l1.val : 0;
            int b = l2!=null ? l2.val : 0;

            sum = carry + a + b;
            carry = sum /10;

            sum = sum % 10;

            currentNode.next = new ListNode(sum);
            currentNode = currentNode.next;

            if(l1!=null) l1 = l1.next;
            if(l2!=null) l2 = l2.next;
        }
        if(carry>0){
            currentNode.next = new ListNode(carry);
        }
        return currentNodeHead.next;

    }


    public static void main(String[] args) {
        ListNode l1= new ListNode(3 );
        ListNode l2= new ListNode(4 );
        ListNode l3= new ListNode(2 );
        ListNode la= new ListNode(4 );
        ListNode lb= new ListNode(6);
        ListNode lc= new ListNode(5);
        l1.next=l2;l2.next=l3;
        la.next=lb;lb.next=lc;
        AddTwoNumber addTwoNumber = new AddTwoNumber();

        ListNode l = addTwoNumber.addTwoNumbers(l1,la);
        System.out.println("answer: "+ l.val);
    }
}
class ListNode {
    int val;
    ListNode next;
    ListNode(int x) { val = x; }
}
