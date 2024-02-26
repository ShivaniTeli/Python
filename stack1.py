MAX_SIZE = 101
a = [0] * MAX_SIZE
top = -1

def push(ele):
    global top
    for i in ele:
        if top <= MAX_SIZE - 1:
            top += 1
            a[top] = i
            print(f"Pushed: {i}")
        else:
            print(f"Stack is full. Cannot push: {i}")

def pop():
    global top
    if top >= 0:
        ele = a[top]
        top -= 1
        print(f"Popped: {ele}")
        return ele
    else:
        print("Stack is empty. Cannot pop.")
        return -1

print(push([10,22,130,40,50]))
print(pop())