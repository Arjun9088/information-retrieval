class Term:
    def __init__(self, item, frequency: int = 1):
        self.item = item
        self.frequency = frequency

    def __eq__(self, other):
        if isinstance(other, Term):
            return self.item == other.item
        return False

    def __hash__(self):
        return hash(self.item)

    def increment_freq(self):
        self.frequency = self.frequency + 1

    def __repr__(self):
        return f"({self.item}, {self.frequency})"


class Posting:
    def __init__(self, value: int, next_p=None):
        self.next_p = next_p
        self.value = value


class PostingsList:

    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, node: Posting):
        if self.head is None:
            self.head = node
            self.tail = node

        else:
            self.tail.next_p = node
            self.tail = node
        return self

    def print(self):
        if self.head is None:
            print("Empty list")
            return
        curr = self.head
        while curr is not None:
            if curr.next_p is None:
                print(f"{curr.value}", end="\t")
            else:
                print(f"{curr.value}->", end="")
            curr = curr.next_p
        print()

    def sort(self):
        """ Implement Merge sort """

    def __repr__(self):
        if self.head is None:
            return ""
        curr = self.head
        output = ""
        while curr is not None:
            if curr.next_p is not None:
                output = output + str(curr.value) + "->"
            else:
                output = output + str(curr.value)
            curr = curr.next_p
        return output


def intersect_postings(list1: PostingsList, list2: PostingsList) -> PostingsList:
    result_list = PostingsList()
    curr_1 = list1.head
    curr_2 = list2.head

    while curr_1 is not None and curr_2 is not None:
        if curr_1.value == curr_2.value:
            result_list.append(Posting(curr_1.value))
            curr_1 = curr_1.next_p
            curr_2 = curr_2.next_p
        elif curr_1.value < curr_2.value:
            curr_1 = curr_1.next_p
        else:
            curr_2 = curr_2.next_p
    return result_list
