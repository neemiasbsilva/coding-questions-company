'''
    Implement a queue using two stacks. 
    Recall that a queue is a FIFO (first-in, first-out) data
    structure with the following methods: enqueue, which inserts
    an element into the queue, and dequeue, which removes it.
'''

stack1 = []
stack2 = []
def enqueue(element):
    stack1.append(element)

def dequeue():
    if len(stack2) == 0:
        if len(stack1) == 0: return "Can not dequeue because queue is empty"
            
        while len(stack1) > 0:
            p = stack1.pop()
            stack2.append(p)
    
    return stack2.pop()


def main():

    for i in range(10):
        enqueue(i)

    print("The queue: {}".format(stack1))
    dequeue()
    print("The queue: {}".format(stack1))




if __name__ == "__main__":
    main()
