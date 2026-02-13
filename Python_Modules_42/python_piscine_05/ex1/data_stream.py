#!/usr/bin/env python3
from abc import ABC, abstractmethod
from typing import Any, List, Dict, Optional


class DataStream(ABC):

    """
    Abstract base class for different types of data streams.

    Variables:
        - stream_id: unique identifier for the stream
        - stats: dictionary to store stream statistics

    Functionality:
        - Defines the interface for processing a batch of data via
          process_batch (abstract).
        - Provides default implementations for filter_data (returns data as is)
          and get_stats (returns stats dictionary).
    """

    def __init__(self, stream_id: str) -> str:

        self.stream_id = stream_id
        self.stats = {}

    @abstractmethod
    def process_batch(self, data: list[Any]) -> str:
        """
        Process a single batch of data specific to the stream type.

        Variables:
            - data: a batch of data (list, dict, or other appropriate
            structure)

        Functionality:
            - Must be implemented in subclasses to handle type-specific
              processing and validation.

        Returns:
            - Typically returns a tuple of (stream type name, count of items
              processed)
        """
        return self.stats

    def filter_data(self, data: list[Any], crit: Optional[str] = None) -> Dict:
        """
        Filter a batch of data based on criteria.

        Variables:
            - data: batch of data
            - crit: optional string defining filter criteria

        Functionality:
            - Default implementation returns the data unmodified.
            - Can be overridden in subclasses to apply filtering logic.

        Returns:
            - List: filtered data (default is the original data)
        """
        return self.stats

    def get_stats(self) -> Dict:
        return self.stats


class SensorStream(DataStream):

    """
    Concrete implementation of DataStream for environmental sensor data.

    Functionality:
        - Processes batches of dictionary data containing 'temp', 'humidity',
          and 'presure'.
        - Validates required keys are present.
        - Prints a summary of readings processed and average temperature.
    """

    def __init__(self, stream_id: str) -> Any:

        self.stream_id = stream_id
        self.stats = {}

    def process_batch(self, data: List) -> str:

        """
        Process a batch of sensor readings.

        Variables:
            - data: dictionary with keys 'temp', 'humidity', 'presure'

        Functionality:
            - Validates keys exist
            - Prints initialization, batch content, and summary info

        Returns:
            - Tuple[str, int]: ('Sensor', number of readings processed)
        """

        if not isinstance(data, dict):
            raise Exception

        required_keys = ["temp", "humidity", "presure"]
        i = 0
        for key in data:
            if key not in required_keys:
                raise Exception
            i += 1

        print("Initializing Sensor Stream...")
        print(f"{self.stream_id}, Type: Enviromental Data")
        print("Procesing sensor batch:", data)
        print(f"Sensor analysis: {i} reading processed, avg temp:"
              f" {data['temp']}\n")

        self.stats["reading"] = i
        self.stats["avg_temp"] = data["temp"]

        return "Sensor", self.stats


class TransactionStream(DataStream):

    """
    Concrete implementation of DataStream for financial transaction data.

    Functionality:
        - Processes batches of dictionary data containing 'buy' and 'sell'
          lists.
        - Computes total number of operations and net flow.
        - Prints summary of transactions.
    """

    def __init__(self, trans_id: str) -> None:

        self.trans_id = trans_id
        self.stats = {}

    def process_batch(self, data: Dict) -> Any:

        """
        Process a batch of transactions.

        Variables:
            - data: dictionary with 'buy' and 'sell' keys, each containing
              list of amounts

        Functionality:
            - Calculates total operations and net flow
            - Prints initialization, batch content, and summary info

        Returns:
            - key + dict information
        """

        if not isinstance(data, dict):
            raise Exception

        required_keys = ["buy", "sell"]
        i = 0
        for key in data:
            if key not in required_keys:
                raise Exception
            i += 1

        total_ops = 0
        net_flow = 0
        high_trans = 0
        for key in data:
            values = data[key]
            for cost in values:
                if cost < 0:
                    cost *= -1
                total_ops += 1
                if key == "buy":
                    net_flow -= cost
                elif key == "sell":
                    net_flow += cost
                if cost > 200:
                    high_trans += 1

        print("Initializing Transaction Stream...")
        print(f"{self.trans_id}, Type: Financial Data")
        print("Procesing transaction batch:", data)
        print(f"Transaction analysis: {total_ops} operations, "
              f"net flow: {net_flow} units\n")

        self.stats["operations"] = total_ops
        self.stats["high"] = high_trans

        return "Transaction", self.stats


class EventStream(DataStream):

    """
    Concrete implementation of DataStream for system event data.

    Functionality:
        - Processes batches of list data containing predefined actions
          ['login', 'error', 'logout', 'fast_travel'].
        - Counts total events and number of errors.
        - Prints summary information.
    """

    def __init__(self, event_id: str) -> None:

        self.event_id = event_id
        self.stats = {}

    def process_batch(self, data: list) -> Any:

        """
        Process a batch of system events.

        Variables:
            - data: list of event strings

        Functionality:
            - Validates events against allowed actions
            - Counts total events and errors
            - Prints initialization, batch content, and summary info

        Returns:
            - Tuple[str, int]: ('Event', event_count)
        """

        if not isinstance(data, list):
            raise Exception

        required_actions = ["login", "error", "logout", "fast_travel"]
        event_count = 0
        error_count = 0
        for word in data:
            found = False
            for action in required_actions:
                if word == action:
                    found = True
                    break
            if not found:
                raise Exception

            event_count += 1

        for word in data:
            if word == "error":
                error_count += 1

        print("Initializing Event Stream...")
        print(f"{self.event_id}, Type: system Events")
        print("Procesing event batch:", data)
        print(f"Event analysis: {event_count} events, "
              f"{error_count} error detected\n")

        self.stats["event_count"] = event_count
        self.stats["error_count"] = error_count

        return "Event", self.stats


class StreamProcessor:

    """
    Manages multiple DataStream objects and processes data batches
    polymorphically.

    Variables:
        - streams: list of DataStream instances
        - data_batches: list of batches to be processed

    Functionality:
        - Iterates over each batch, attempts to process it through available
          streams
        - Handles errors if no stream can process a batch
        - Collects summary data and prints a report of all streams processed
    """

    def process_streams(self, streams: int, data_batches: list) -> None:

        """
        Process multiple data batches through polymorphic streams.

        Variables:
            - streams: list of DataStream instances
            - data_batches: list of data batches

        Functionality:
            - Attempts each batch on each stream until one succeeds
            - Collects counts of processed items per stream type
            - Prints batch summary and final throughput report

        Returns:
            - None: output is printed to standard output
        """
        print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

        complete_data = {}

        for batch in data_batches:
            processed = False
            for stream in streams:
                try:
                    key, count = stream.process_batch(batch)
                    processed = True
                    break
                except Exception:
                    pass
            if processed is False:
                print("Error processing stream in all Streams classes\n")
            else:
                complete_data[key] = count

        print("=== Polymorphic Stream Processing ===")

        print("\nBatch 1 Results:")
        reads = 0
        problem_temp = 0
        operations = 0
        high = 0
        event_count = 0
        error_count = 0
        for key in complete_data:
            if key == "Sensor":
                reads = complete_data[key]["reading"]
                if complete_data[key]["avg_temp"] > 60:
                    problem_temp += 1
                print(f"- {key} data = {reads} reading processed")
            elif key == "Transaction":
                operations = complete_data[key]["operations"]
                high = complete_data[key]["high"]
                print(f"- {key} data = {operations} operations"
                      " processed")
            elif key == "Event":
                event_count = complete_data[key]["event_count"]
                error_count = complete_data[key]["error_count"]
                print(f"- {key} data = {event_count} events"
                      " processed\n")

        print("\nStream filtering active: High-priority data only")
        print(f"Filtered results: {error_count} critical sensor alerts,"
              f" {high} large transaction, {problem_temp} problematic average"
              " temperature\n")

        print("All streams processed successfully. Nexus throughput optimal.")


if __name__ == "__main__":

    streams = [
        SensorStream("SENSOR_001"),
        TransactionStream("TRANS_001"),
        EventStream("EVENT_001")
        ]
    batches = [
        {"temp": 22.5, "humidity": 65, "presure": 1013},
        {"buy": [100, 50], "sell": [-750]},
        ["login", "error", "logout", "error"],
        ["not_valid_string"]
        ]

    processor = StreamProcessor()
    processor.process_streams(streams, batches)
