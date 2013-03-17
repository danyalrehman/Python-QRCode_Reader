def convert_to_binary(value, length):
    """ This function will take any integer and return a string
    of binary codes of the given length. It is guaranteed that
    the user inputted integer is a non-negative number, and if
    the given length is shorter than the minimum length of the
    binary code, it will return the shortest possible correct
    binary code.

        for example:

        >>> print convert_to_binary(100, 5)
        1100100

        >>> print convert_to_binary(100, 10)
        0001100100

    """

    n = 0
    power2 = []
    binarylist = []
    # This while loop detemines the highest power of 2
    # that fits into the value (and every power below it)
    # and appends those values to the empty list power2.
    while 2 ** n <= value:
        power2.append(n)
        n += 1
    n -= 1
    # This for loop starts from the highest power of 2 possible
    # within the value, and everytime the that power of 2 is
    # subtracted from the value, and the remainder, from smaller powers,
    # until the value becomes 0, and the binary number is
    # determined.
    for i in power2:
        if value - (2 ** n) >= 0:
            binarylist.append(1)
            value -= (2 ** n)
        else:
            binarylist.append(0)
        n -= 1
    x = ""
    # This for loop converts the binary number into a string.
    for i in binarylist:
        x += str(i)
    count = 0
    # The rest of the function sets the length of the binary string.
    for i in x:
        count += 1
    numzeros = length - count
    y = ""
    while numzeros > 0:
        y += "0"
        numzeros -= 1
    return y + x

def convert_to_decimal(value):
    """ This function will take any string of binary code
    and convert it into an integer the binary code represents.
    If the number that is put in is not a binary number, it
    will print "This is not a binary number, please try again."

        For example:

        >>> print convert_to_decimal("110101")
        53

        >>> print convert_to_decimal("5")
        This is not a binary number, please try again.

    """


    for index in value:
        if index != "1" or "0":
            return "This is not a binary number. Please try again."

    final_value = 0
    sublist = []
    for i in value:
        if i == "1":
            sublist.append(1)
        else:
            sublist.append(0)
    n = 0
    count = -1
    while (-1 * len(sublist)) < n:
        n -= 1
        count += 1
        if sublist[n] == 1:
            final_value += 2 ** count
    return final_value

def create_table():
    """ This function creates a dictionary with key-value pairs
    of keys as characters, and values as their integer values, which
    also can be expressed as binary codes.
    """

    dict1 = {}
    count = 0
    # This while loop adds all numbers to the dictionary, as
    # values and keys themselves.
    while count < 10:
        dict1[str(count)] = count
        count += 1
    dict1["A"] = 10
    dict1["B"] = 11
    dict1["C"] = 12
    dict1["D"] = 13
    dict1["E"] = 14
    dict1["F"] = 15
    dict1["G"] = 16
    dict1["H"] = 17
    dict1["I"] = 18
    dict1["J"] = 19
    dict1["K"] = 20
    dict1["L"] = 21
    dict1["M"] = 22
    dict1["N"] = 23
    dict1["O"] = 24
    dict1["P"] = 25
    dict1["Q"] = 26
    dict1["R"] = 27
    dict1["S"] = 28
    dict1["T"] = 29
    dict1["U"] = 30
    dict1["V"] = 31
    dict1["W"] = 32
    dict1["X"] = 33
    dict1["Y"] = 34
    dict1["Z"] = 35
    dict1[" "] = 36
    dict1["$"] = 37
    dict1["%"] = 38
    dict1["*"] = 39
    dict1["+"] = 40
    dict1["-"] = 41
    dict1["."] = 42
    dict1["/"] = 43
    dict1[":"] = 44
    return dict1

def encode_text(message):
    """ This function will take any string and convert the string
    into an equivalent string of binary code in a unique process,
    and will return a binary string of either multiple of 11 - digit
    or multiples of 11 plus 6 more digit long binary code.

        For example:

        >>> print encode_text("HI")
        01100001111

        >>> print encode_text("hi")
        01100001111
        
    """

    message = message.upper()
    dict1 = create_table()
    count = 0
    final_string = ""
    sublist = []
    even = len(message) / 2
    odd = len(message) % 2
    # This while loop appends empty lists to the sublist, and the number of
    # indices in the sublist represent the number of letters in the message
    while count < even:
        sublist.append([])
        count += 1
    count = 0
    # This for loop takes all characters in the message, two at a time, and
    # applies mathematical functions and outputs a certain binary code of
    # multiple of 11 digits
    for index in sublist:
        if count < len(message):
            first_letter = message[count]
            second_letter = message[count + 1]
            binary_code = convert_to_binary((dict1[first_letter] * 45)
                                            + dict1[second_letter], 11)
            final_string += str(binary_code)
            count += 2
    # IF the message has odd number of characters, the last character will
    # undergo a different mathematical function and added to the final_string.
    if odd == 1:
        last_letter = message[-1]
        binary_code = convert_to_binary(dict1[last_letter], 6)
        final_string += str(binary_code)
    return final_string

def make_data(message):
    """ This function will take a string and convert it into a 104 digit
    long binary code that will be stored in the QRgrid.

        For example:

        >>> print make_data("HELLO WORLD")
        001000000101101100001011011110  \n
        001101000101110010110111000100  \n   (all in single line)
        110101000011010000001110110000  \n
        01000111101100

    """

    # The final_string is already set to have (17 plus a number of
    # binary characters the message is supposed to hold)
    # characters to begin with.
    final_string = "0010" + convert_to_binary(len(message), 9)\
                   + encode_text(message) + "0000"
    # "0"s are added to the final_string until it is divisible by 8.
    if len(final_string) % 8 != 0:
        count = 0
        while count < len(final_string) % 8:
            final_string += "0"
    # This while loop adds "11101100" and "00010001" until the number
    # of characters reach 104 characters
    while len(final_string) < 104:
        final_string += "11101100"
        if len(final_string) < 104:
            final_string += "00010001"
    return final_string

class Grid:
    """ The Grid class is a combination of internal functions that
    make up the QRcode representing a string of characters.
    """

    def __init__(self, size):
        """ This function creates a grid of size (the inputted
        positive integer) by size dimensions, with all coordinates
        unassigned as X.
        """

        sublist = []
        count = 0
        # This while loop sets a size number of rows
        while count < size:
            sublist.append([])
            count += 1
        # This for loop sets a size number of columns and sets
        # all positions the value of X.
        for index in sublist:
            count = 0
            while count < size:
                index.append("X")
                count += 1
        self.size = sublist

    def __str__(self):
        """ This function returns a string equivalent of the grid.

            For exmaple:
            >>> c = qrcode.Grid(4)
            >>> print c
            XXXX
            XXXX
            XXXX
            XXXX
            
        """

        count = 0
        returnstring = ""
        # All of the loops are converting each index of the grid (a list)
        # into strings, and adding them.
        for index in self.size:
            gridstring = ""
            for index in index:
                returnstring += str(index)
                gridstring += str(index)
            print gridstring
            count += 1
            if count != len(self.size):
                returnstring += "\n"
        return returnstring

    def set(self, x_pos, y_pos, value):
        """ Set a value of a specific position on the grid,
        where x_pos and y_pos resembles the x position and
        y position respectively, and the value can be either 0
        or 1 or X.

            For example:
            >>> c.set(2,2,1)
            >>> print c
            XXXX
            XXXX
            XX1X
            XXXX

        """

        self.size[y_pos][x_pos] = value

    def add_square(self, x_pos, y_pos, size, value):
        """ Set a value to filled in square within the grid,
        where the x_pos and y_pos refer to the position of the
        top left corner of the square and size being the length
        of the side of the square.

            For example:
            >>> c.add_square(0,0,2,1)
            >>> print c
            11XX
            11XX
            XXXX
            XXXX

        """

        count2 = 0
        # Sets the square.
        while count2 < size:
            count = 0
            while count < size:
                self.size[y_pos + count2][x_pos + count] = value
                count += 1
            count2 += 1

    def add_checksum(self):
        """ Set the checksum values to appropriate positions
        of the grid.
        """
        
        count = 0
        binstring = "010110110111010"
        while count < 6:
            self.size[count][8] = binstring[count]
            count += 1
        self.size[7][8] = binstring[6]
        self.size[8][8] = binstring[7]
        count = 14
        count2 = 8
        while count2 < 15:
            self.size[count][8] = binstring[count2]
            count += 1
            count2 += 1

        count = -1
        count2 = 0
        while count > -9:
            self.size[8][count] = binstring[count2]
            count -= 1
            count2 += 1
        self.size[8][-14] = binstring[5]
        count = -16
        count2 = 9
        while count2 < 15:
            self.size[8][count] = binstring[count2]
            count -= 1
            count2 += 1

    def make_grid(self):
        """ Set an empty QRcode (meaning it contains position
        detection patterns, timing patterns, and checksum values.
        No character binary code is present within the QRcode.
        """

        self.add_square(0, 0, 8, 0)
        self.add_square(0, 0, 7, 1)
        self.add_square(1, 1, 5, 0)
        self.add_square(2, 2, 3, 1)
        self.add_square(0, 13, 8, 0)
        self.add_square(0, 14, 7, 1)
        self.add_square(1, 15, 5, 0)
        self.add_square(2, 16, 3, 1)
        self.add_square(13, 0, 8, 0)
        self.add_square(14, 0, 7, 1)
        self.add_square(15, 1, 5, 0)
        self.add_square(16, 2, 3, 1)
        count = 8
        while count < 13:
            if count % 2 == 1:
                value = 0
            else:
                value = 1
            self.set(count, 6, value)
            count += 1
        count = 8
        while count < 13:
            if count % 2 == 1:
                value = 0
            else:
                value = 1
            self.set(6, count, value)
            count += 1
        self.set(8, 13, 1)
        self.add_checksum()

if __name__ == "__main__":
    x = Grid(21)
    x.make_grid()