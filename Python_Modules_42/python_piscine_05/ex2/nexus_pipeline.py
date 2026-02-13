#!/usr/bin/env python3
from abc import ABC
from typing import Any, List, Dict, Union, Protocol


class ProcessingStage(Protocol):

    """
    Protocol defining a generic processing stage interface.

    Functionality:
        - Ensures any stage implements a `process(data)` method.
    """

    def process(self, data: Any) -> Any:

        """
        Process the input data.

        Variables:
            - data: any type of input data

        Functionality:
            - Must be implemented in concrete stages.

        Returns:
            - Processed data (type depends on stage)
        """
        pass


class ProcessingPipeline(ABC):

    """
    Abstract class for a data processing pipeline.

    Variables:
        - pipeline_id: unique identifier for the pipeline
        - stages: list of ProcessingStage instances added to the pipeline

    Functionality:
        - Stores and manages multiple processing stages
        - Runs data sequentially through all stages
    """

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id
        self.stages = []

    def add_pipeline(self, stage: ProcessingStage) -> None:

        """
        Add a processing stage to the pipeline.

        Variables:
            - stage: object implementing ProcessingStage protocol

        Functionality:
            - Appends the stage to the stages list

        Returns:
            - None
        """
        self.stages = self.stages + [stage]

    def process(self, data: Any) -> Any:

        """
        Execute the pipeline on input data.

        Variables:
            - data: input data to be processed through the pipeline

        Functionality:
            - Sequentially applies each stage to the data
            - Catches exceptions at any stage and stops processing

        Returns:
            - final processed data, or None if an error occurred
        """
        current_data = data
        for stage in self.stages:
            try:
                current_data = stage.process(current_data)
            except Exception as e:
                print(e)
                return None

        return current_data


class InputStage():

    """
    First stage of the pipeline for input validation and adaptation.

    Variables:
        - adapters: list of adapter objects capable of processing specific data
        types

    Functionality:
        - Tries each adapter on the input until one succeeds
        - Raises an exception if no adapter can handle the input
    """

    def __init__(self, adapters: List) -> None:
        self.adapters = adapters

    def process(self, data: Any) -> Any:

        """
        Validate and adapt input data.

        Variables:
            - data: raw input data

        Functionality:
            - Iterates through adapters attempting to process the data
            - Stops at the first successful adapter
            - Raises exception if no adapter can process the data

        Returns:
            - Adapted data in a standardized format
        """

        for adapter in self.adapters:
            try:
                adapted_data = adapter.process(data)
                return adapted_data
            except Exception:
                continue
        raise Exception("Error detected in Stage 1:"
                        " The information cannot be treated as any of the"
                        " adapters\n")


class TransformStage():

    """
    Second stage of the pipeline for data transformation.

    Functionality:
        - Modifies or enriches data depending on its type
        - Supports dict, list, and string inputs
        - Adds validation, metadata, parsing, or aggregation
    """

    def process(self, data: Dict) -> Dict:

        """
        Transform input data into standardized format.

        Variables:
            - data: input data (dict, list, or string)

        Functionality:
            - Dict: adds validation flag and metadata
            - String: parses CSV-like data into list
            - List: aggregates numbers into sum, count, avg
            - Raises exception if format unsupported

        Returns:
            - Transformed or enriched data
        """
        if isinstance(data, dict):
            data["validate"] = True
            data["metadata"] = "adapted"
            print("Transform: Enriched with metadata and validation")

        elif isinstance(data, str):
            values = []
            temp = ""
            for char in data:
                if char == ",":
                    values = values + [temp]
                    temp = ""

                else:
                    temp += char

            if temp:
                values = values + [temp]

            data = values
            print("Transform: Parsed and structured data")

        elif isinstance(data, list):
            total = 0
            count = 0
            for num in data:
                total += num
                count += 1

            data = {"sum": total, "count": count, "avg": total / count
                    if count else 0}
            print("Transform: Aggregated and filtered")

        else:
            raise Exception("Error detected in Stage 2: Invalid data format")

        return data


class OutputStage():

    """
    Final stage of the pipeline for output formatting and delivery.

    Functionality:
        - Prints summaries or formatted output depending on data type
        - Handles dict, list, and aggregated dict outputs
    """

    def process(self, data: dict) -> str:

        """
        Format and print processed data.

        Variables:
            - data: processed data from previous stages

        Functionality:
            - Dict with 'sensor': prints reading
            - List: prints number of actions processed
            - Aggregated dict: prints summary statistics
            - Raises exception on failure

        Returns:
            - The input data, unchanged
        """
        try:
            if (isinstance(data, dict) and "sensor" in data and "value"
                    in data and "unit" in data):
                print(f"Output: Processed {data['sensor']} reading: "
                      f"{data['value']} ({data['unit']})\n")

            elif isinstance(data, list):
                i = 0
                for element in data:
                    i += 1
                print(f"Output: User activity logged: {i} actions processed\n")

            elif isinstance(data, dict) and "sum" in data:
                print(f"Output: Stream ummary: {data['count']} readings, avg: "
                      f"{data['avg']:.1f} ºC\n")
            return data
        except Exception:
            raise Exception("Error detected in Stage 3: leaking information")


class JSONAdapter(ProcessingPipeline):

    """
    Adapter for handling JSON-formatted input data.

    Functionality:
        - Validates input is a dict
        - Prints confirmation of processing
        - Raises exception if input not dict
    """

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:

        """
        Process JSON data.

        Variables:
            - data: input JSON dictionary

        Functionality:
            - Checks type
            - Prints input for logging
            - Returns input unchanged

        Returns:
            - dict: processed JSON data
        """
        if isinstance(data, dict):
            print("Processing JSON data through pipeline...")
            print("Imput: ", data)
            return data
        else:
            raise Exception


class CSVAdapter(ProcessingPipeline):

    """
    Adapter for handling CSV-formatted input data.

    Functionality:
        - Validates input is a string
        - Prints confirmation of processing
        - Raises exception if input not string
    """

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:

        """
        Process CSV data.

        Variables:
            - data: input CSV string

        Functionality:
            - Checks type
            - Prints input for logging
            - Returns input unchanged

        Returns:
            - str: processed CSV string
        """
        if isinstance(data, str):
            print("Processing CSV data through same pipeline...")
            print("Input: ", data)
            return data
        else:
            raise Exception


class StreamAdapter(ProcessingPipeline):

    """
    Adapter for handling real-time numeric data streams.

    Functionality:
        - Validates input is a list of numbers
        - Prints confirmation of processing
        - Raises exception if input contains non-numeric elements
    """

    def __init__(self, pipeline_id: str) -> None:
        self.pipeline_id = pipeline_id

    def process(self, data: Any) -> Union[str, Any]:

        """
        Process numeric stream data.

        Variables:
            - data: list of numbers

        Functionality:
            - Checks all elements are int or float
            - Prints input confirmation
            - Returns input unchanged

        Returns:
            - list: numeric stream data
        """
        if isinstance(data, list):
            for numb in data:
                if not isinstance(numb, (int, float)):
                    raise Exception("Invalid Data Stream")
            print("Processing Stream data through same pipeline...")
            print("Input: Real-time sensor stream")
            return data
        else:
            raise Exception("Invalid Data Stream")


class NexusManager():

    """
    Manages the setup and execution of the multi-format data processing
    pipeline.

    Functionality:
        - Initializes a main processing pipeline with input, transform, and
        output stages
        - Handles JSON, CSV, and numeric stream data
        - Demonstrates error handling with faulty input
    """

    def process(self, data: list) -> None:

        """
        Run the pipeline on provided data.

        Variables:
            - data: input data batch

        Functionality:
            - Executes the pipeline, catching errors
            - Prints error message on failure

        Returns:
            - None
        """
        try:
            return self.pipeline.process(data)
        except Exception:
            print("Error detected: pipeline failed")
            return None

    def setup(self):

        """
        Set up and demonstrate the Nexus processing pipeline.

        Functionality:
            - Initializes pipeline capacity and stages
            - Adds InputStage, TransformStage, OutputStage
            - Processes example JSON, CSV, and stream data
            - Demonstrates error handling with invalid data

        Returns:
            - None
        """

        self.capacity = 1000
        print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")
        print("Initializing Nexus Manager...")
        print(f"Pipeline capacity: {self.capacity} streams/second\n")

        self.pipeline = ProcessingPipeline("MAIN_PIPELINE")

        input_stage = InputStage(
            [JSONAdapter(self.pipeline.pipeline_id),
             CSVAdapter(self.pipeline.pipeline_id),
             StreamAdapter(self.pipeline.pipeline_id)]
             )

        self.pipeline.add_pipeline(input_stage)
        self.pipeline.add_pipeline(TransformStage())
        self.pipeline.add_pipeline(OutputStage())

        print("Creating Data Processing Pipeline...")
        print("Stage 1: Input validation and parsing")
        print("Stage 2: Data transformation and enrichment")
        print("Stage 3: Output formatting and delivery\n")

        print("=== Multi-Format Data Processing ===\n")

        json_data = {"sensor": "temp", "value": 23.5, "unit": "C"}
        csv_data = "user, action, timestamp"
        stream_data = [22, 23, 21, 24.4]

        self.process(json_data)
        self.process(csv_data)
        self.process(stream_data)

        print("=== Error Recovery Test ===")
        print("Simulating pipeline failure...")

        error_data = [22, 4, "hey", "cool"]

        self.process(error_data)


if __name__ == "__main__":

    manager = NexusManager()
    manager.setup()
