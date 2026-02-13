#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List


class DataProcessor(ABC):

    """
    Abstract base class for all data processors. Defines the interface for
    processing, validating, formatting, and error handling of data.

    Methods:
        - error(): Handles errors for invalid data.
        - format_output(data): Formats and prints the processed data.
        - validate(data): Validates the incoming data according to processor
        type.
        - process(data): Main entry point to process the data using validate
        and format_output.

    Usage:
        Subclass this class and implement all abstract methods.
    """

    @abstractmethod
    def error(self) -> None:

        """
        Handles errors when the data cannot be processed.

        Functionality:
            - Prints a message indicating the data is not computable.

        Returns:
            - None
        """

        print("Parameter not computable.\n")

    @abstractmethod
    def format_output(self, data: Any) -> None:

        """
        Formats and prints the output data.

        Variables:
            - data: input data to process, could be numeric, text, or log.

        Functionality:
            - Count elements, classify as numbers or strings, and print
            summary.

        Returns:
            - None
        """

        print("Processing all formats")

        number_count = 0
        char_count = 0
        total_count = 0
        for element in data:
            try:
                element = element + 0
                number_count += 1
            except Exception:
                char_count += 1
            total_count += 1

        print(f"Output: Processed {total_count} elements: Numbers:"
              f" {number_count}, Strings: {char_count}\n")

    @abstractmethod
    def validate(self, data: Any) -> None:

        """
        Validates the input data.

        Variables:
            - data: input data to check

        Functionality:
            - Iterates through data elements and checks basic validity.
            - Raises Exception if data is invalid (e.g., contains null
            character).

        Returns:
            - None
        """

        for element in data:
            if element == "\0":
                raise Exception

    @abstractmethod
    def process(self, data: Any) -> None:

        """
        Main method to process data using validation and formatting.

        Variables:
            - data: input data to process

        Functionality:
            - Calls validate() to check data
            - Calls format_output() to display results
            - If validation fails, calls error()

        Returns:
            - None
        """

        print("Procesing data:", data)
        try:

            self.validate(data)
            self.format_output(data)

        except Exception:
            self.error()


class NumericProcessor(DataProcessor):

    """
    Data processor specialized for numeric data.

    Methods:
        - error(): Prints numeric-specific error.
        - format_output(data): Prints sum and average of numeric data.
        - validate(data): Ensures all elements are numeric.
        - process(data): Initializes and processes numeric data.
    """

    def error(self) -> None:

        print("Parameter not computable. Check if all the parameters are"
              " numbers\n")

    def format_output(self, data: List) -> None:

        sumatory = 0
        i = 0
        for element in data:
            i += 1
            sumatory += element

        average = sumatory / i

        print(f"Output: Processed {i} numeric values, sum= {sumatory:.2f},"
              f"avg={average:.2f}\n")

    def validate(self, data: List) -> None:

        for num in data:
            x = num + 0
        x = ""
        print(x, end="")
        print("Validation: Numeric data verified")

    def process(self, data: List) -> None:

        print("Initializing Numeric Processor...")
        super().process(data)


class TextProcessor(DataProcessor):

    """
    Data processor specialized for text data.

    Methods:
        - error(): Prints text-specific error.
        - format_output(data): Counts words and letters and prints results.
        - validate(data): Ensures all elements are strings.
        - process(data): Initializes and processes text data.
    """

    def error(self) -> None:

        print("Parameter not computable. Check if all the parameters are"
              " strings or chars\n")

    def format_output(self, data: List) -> None:

        word_count = 0
        letter_count = 0
        for word in data:
            word_count += 1
            for letter in word:
                letter_count += 1

        print(f"Output: Processed text values: {letter_count} chars,"
              f" {word_count} words\n")

    def validate(self, data: List) -> None:

        x = 0
        for element in data:
            try:
                element = element + 0
                raise Exception
            except TypeError:
                x += 1
        x = ""
        print(x, end="")
        print("Validation: String data verified")

    def process(self, data: List) -> None:

        print("Initializing Text Processor...")
        super().process(data)


class LogProcessor(DataProcessor):

    """
    Data processor specialized for log strings.

    Methods:
        - error(): Prints log-specific error.
        - format_output(data): Parses log level and content, prints formatted
        message.
        - validate(data): Ensures log contains a colon separating level and
        message.
        - process(data): Initializes and processes log data.
    """

    def error(self) -> None:

        print("Parameter not computable. Check if all the parameter is a"
              " log.\n")

    def format_output(self, data: str) -> None:

        log_entry = ""
        data_entry = ""
        after_colon = False
        for char in data:
            if char == ":" and after_colon is False:
                after_colon = True
                continue
            if after_colon is False:
                log_entry = log_entry + char
            else:
                data_entry = data_entry + char
        if log_entry == "ERROR":
            tag = "[ALERT]"
        elif log_entry == "WARNING":
            tag = "[WARN]"
        elif log_entry == "INFO":
            tag = "[INFO]"
        else:
            raise Exception
        print(f"Output: {tag} {log_entry} level detected: {data_entry}\n")

    def validate(self, data: str) -> None:

        found_colon = False

        try:
            data = data + ""
        except Exception:
            raise Exception

        for char in data:
            if char == ":":
                found_colon = True
                break

        if found_colon is False:
            raise Exception

        print("Validation: Log data verified")

    def process(self, data: str) -> None:

        print("Initializing Log Processor...")
        super().process(data)


def ft_len(array: List) -> int:

    """
    Calculates the number of elements in a list.

    Variables:
        - array: list of elements whose length will be calculated.

    Functionality:
        - Iterates through the list and counts each element manually
          using a counter variable.

    Returns:
        - int: total number of elements in the list.
    """

    i = 0
    for element in array:
        i += 1
    return i


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    num = NumericProcessor()
    text = TextProcessor()
    log = LogProcessor()
    num.process([4, 5, 3, 21])
    text.process(["a", "Hello", "five", "twenty"])
    log.process("ERROR: Good Morning")

    print()
    print("=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...\n")
    processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
    data_list = [
        [1, 2, 3],
        ["Hello", "World", "Fortytwo"],
        "INFO: System ready"
    ]

    result_number = 1
    i = 0
    while i < ft_len(processors):
        print(f"Result {result_number}:", end="")
        processors[i].format_output(data_list[i])
        result_number += 1
        i += 1

    print("Foundation systems online. Nexus ready for advanced streams.")
