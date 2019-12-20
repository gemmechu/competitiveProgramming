package Day8;

public class DeleteNode {

    public  static void main(String[] args){
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(1);
        ListNode c = new ListNode(2);
        ListNode d = new ListNode(3);
        ListNode e = new ListNode(3);

        a.next=b;
        b.next=c;
        c.next=d;
        d.next=e;

        DeleteNode deleteNode= new DeleteNode();
        ListNode sorted = deleteNode.deleteDuplicates(a);
        while (true){

            System.out.println(sorted.val);

            if(sorted.next==null){
                break;
            }

            sorted=sorted.next;
        }
       // deleteNode.deleteNode(b);





    }
    public void deleteNode(ListNode node) {
        ListNode temp= node.next;
        node.val = temp.val;
        node.next=temp.next;
        temp.next=null;
    }
    public ListNode deleteDuplicates(ListNode head)     {
        ListNode removedList=head;
        ListNode curr = head;
        while (curr!=null){


            ListNode temp = curr;

            while(temp!=null && temp.val==curr.val) {
                temp = temp.next;
            }

            curr.next = temp;
            curr = curr.next;

        }
        return  removedList;
    }
}
