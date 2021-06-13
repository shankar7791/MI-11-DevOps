class Node :
    def __init__(self, data):
        self.data = data ;
        self.next = None ;

class MinMax :
    def __init__(self):
        self.head = None;
        self.tail = None;

    def additionNode(self, data):
        newNode = Node(data);

        if(self.head == None):
            self.head = self.tail = newNode;
            self.head.previous = None;
            self.tail.next = None;
        else:
            self.tail.next = newNode;
            newNode.previous = self.tail;
            self.tail = newNode;
            self.tail.next = None;

    def minimumNode(self):
        current = self.head;
        if(self.head == None):
            print("empty list");
            return 0;
        else:
            min = self.head.data;
            while(current!=None):
                if(min>current.data):
                    min = current.data;
                current = current.next;
        return min;

    def maximumNode(self):
        current = self.head;
        if(self.head == None):
            print("empty list");
            return 0;
        else:
            max = self.head.data;
            while(current!=None):
                if(current.data>max):
                    max = current.data;
                current = current.next;
        return max;

dList = MinMax();

dList.additionNode(44);
dList.additionNode(78);
dList.additionNode(100);
dList.additionNode(98);


print("Minimum value node is:"+str(dList.minimumNode()));
print("\nMaximum value node is:"+str(dList.maximumNode()));