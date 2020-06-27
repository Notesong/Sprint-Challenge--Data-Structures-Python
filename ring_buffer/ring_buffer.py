class RingBuffer:
    def __init__(self, capacity):
        self.capacity = capacity
        # keep track of the current item that will
        # be appended
        self.current_position = 0
        # set up an appropriate size list for the ring buffer
        # each element is initialized as None
        self.storage = [None] * capacity

    def append(self, item):
        # reset the current position to 0 if the buffer is full
        if self.current_position >= self.capacity:
            self.current_position = 0
        i = self.current_position
        # overwrite the item in storage's current position to
        # the new item and increment the current position
        self.storage[i] = item
        self.current_position += 1

    def get(self):
        # create a temporary list that will be returned to the caller
        temp_list = []
        # go through the items currently in storage
        for item in self.storage:
            # if they're not None, add them to the temp list and then
            # return the list after looping
            if item is not None:
                temp_list.append(item)
        return temp_list
