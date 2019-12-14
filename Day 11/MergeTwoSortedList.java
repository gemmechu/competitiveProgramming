package Day8;

import java.util.List;

public class MergeTwoSortedList {
    public  static void main(String[] args)
    {
        ListNode a = new ListNode(1);
        ListNode b = new ListNode(1);
        ListNode c = new ListNode(2);
        ListNode d = new ListNode(3);
        ListNode e = new ListNode(4);
        ListNode f = new ListNode(4);
        a.next=c;
        b.next=d;
        c.next=e;
        d.next=f;

        MergeTwoSortedList myclass = new MergeTwoSortedList();
        ListNode mergedList = myclass.mergeTwoLists(a,b);
        ListNode temp= mergedList;
        while (true){

            System.out.println(temp.val);

            if(temp.next==null){
                break;
            }

            temp=temp.next;
        }


    }

    public ListNode mergeTwoLists(ListNode l1, ListNode l2) {

        ListNode result;
        ListNode current;
        // Base cases
        if (l1 == null)
            return l2;

        else if (l2 == null)
            return l1;

        if(l1.val<= l2.val){
            current= l1;
            l1=l1.next;


        }
        else{
            current=l2;
            l2=l2.next;

        }
        result = current;

        while (true){
            if(l1 !=null && l2!=null){
                if(l1.val<= l2.val){
                    current.next=l1;
                    current=l1;
                    l1=l1.next;


                }
                else{
                    current.next=l2;
                    current=l2;
                    l2=l2.next;

                }
                if(l1 == null){
                    current.next=l2;
                    current=l2;

                }
                if(l2 ==null){
                    current.next=l1;
                    current=l1;

                }



            }
            else{
                break;
            }

        }

        return result;

    }


}
