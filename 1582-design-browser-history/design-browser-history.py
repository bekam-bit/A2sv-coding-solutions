class ListNode:
    def __init__(self, val, next=None, prev = None):
        self.val = val
        self.next = next
        self.prev = prev
        
class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = ListNode(homepage)
        self.cur = self.head

    def visit(self, url: str) -> None:
        self.cur.next = None

        self.newNode = ListNode(url)
        self.cur.next = self.newNode
        self.newNode.prev = self.cur
        self.cur = self.newNode
        
    def back(self, steps: int) -> str:
        while self.cur and self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1

        return self.cur.val

    def forward(self, steps: int) -> str:
        while self.cur and self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        
        return self.cur.val


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)