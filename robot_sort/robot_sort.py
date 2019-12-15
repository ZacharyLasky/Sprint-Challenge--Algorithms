class SortingRobot:
    def __init__(self, l):
        """
        SortingRobot takes a list and sorts it.
        """
        self._list = l          # The list the robot is tasked with sorting
        self._item = None       # The item the robot is holding
        self._position = 0      # The list position the robot is at
        self._light = "OFF"     # The state of the robot's light
        self._time = 0          # A time counter (stretch)

    def can_move_right(self):
        """
        Returns True if the robot can move right or False if it's
        at the end of the list.
        """
        return self._position < len(self._list) - 1

    def can_move_left(self):
        """
        Returns True if the robot can move left or False if it's
        at the start of the list.
        """
        return self._position > 0

    def move_right(self):
        """
        If the robot can move to the right, it moves to the right and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position < len(self._list) - 1:
            self._position += 1
            return True
        else:
            return False

    def move_left(self):
        """
        If the robot can move to the left, it moves to the left and
        returns True. Otherwise, it stays in place and returns False.
        This will increment the time counter by 1.
        """
        self._time += 1
        if self._position > 0:
            self._position -= 1
            return True
        else:
            return False

    def swap_item(self):
        """
        The robot swaps its currently held item with the list item in front
        of it.
        This will increment the time counter by 1.
        """
        self._time += 1
        # Swap the held item with the list item at the robot's position
        self._item, self._list[self._position] = self._list[self._position], self._item

    def compare_item(self):
        """
        Compare the held item with the item in front of the robot:
        If the held item's value is greater, return 1.
        If the held item's value is less, return -1.
        If the held item's value is equal, return 0.
        If either item is None, return None.
        """
        if self._item is None or self._list[self._position] is None:
            return None
        elif self._item > self._list[self._position]:
            return 1
        elif self._item < self._list[self._position]:
            return -1
        else:
            return 0

    def set_light_on(self):
        """
        Turn on the robot's light
        """
        self._light = "ON"

    def set_light_off(self):
        """
        Turn off the robot's light
        """
        self._light = "OFF"

    def light_is_on(self):
        """
        Returns True if the robot's light is on and False otherwise.
        """
        return self._light == "ON"

    def sort(self):
        """
        Sort the robot's list.
        """
        # Fill this out

        # start with robots light on so we have a while loop
        # while the robots light is on... robot should be able to move right until the end of the list
        # while the robot can can still move right, the robot should be swapping each card with the card to its right if the card to its right is less than its current card
        # the robot should then move left with the smallest num
        # if the robot cant compare that item, it should swap it for the next card ahead of it
        # once cards are in order, the loop should break
        self.set_light_on()
        # have an item at the beginning to compare to
        self.swap_item()
        # while the sorting light is on...

        while self.light_is_on():
            # if the item can't be compared, the list is sorted
            if self.can_move_right() == False and self.compare_item() == None:
                self.swap_item()
                break
            # while the robot can move right...
            while self.can_move_right():
                # move right
                self.move_right()
                # compare the item in front with item its holding...
                # if the item its holding is greater, swap it for the item in front
                if self.compare_item() == 1:
                    self.swap_item()

            # while robot can move left...
            while self.can_move_left():
                # move left with smallest num
                self.move_left()
                # if the item can't be compared
                if self.compare_item() == None:
                    # swap it at the first index
                    self.swap_item()
                # bring largest num to last index
                    self.move_right()
                    self.swap_item()
                    break
        return self._list


if __name__ == "__main__":
    # Test our your implementation from the command line
    # with `python robot_sort.py`

    l = [5, 4, 3, 2, 1]

    robot = SortingRobot(l)

    robot.sort()
    print(robot._list)
