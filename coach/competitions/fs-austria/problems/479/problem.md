---
id: 479
event: "fs-austria"
year: 2018
rules_year: 2018
quizzes: [{"quiz_id": 45, "year": 2018, "class": "ev", "position": 13}]
type: "single-choice"
time_s: 0
topic: ["electronics"]
options: ["Your infrared thermometer is configured for a wrong radiation emission coefficient", "Two sensor nodes are configured to the same CAN ID", "The can bus is overloaded", "This is an expected result with the given accuracy of the sensors", "The endianness is wrong in the DAQ config"]
answer: "Two sensor nodes are configured to the same CAN ID"
unit: null
rule_refs: []
source: "https://fs-quiz.eu/question/479"
status: "unverified"
verified_by: null
---

# Problem 479

Your car is equipped with one tire temperature sensor node per wheel. They are connected to the DAQ system via common CAN bus.\n Sensor Accuracy is 0.5 degC\n data format is 10-bit unsigned integer; quatisation 0.25 degC/bit, offset 0 degC\n Message Interval is 100ms\n When reviewing the data, you notice the following pattern on one of the logged temperature channels

![](images/479_1.jpg)

Options:
- A) Your infrared thermometer is configured for a wrong radiation emission coefficient
- B) Two sensor nodes are configured to the same CAN ID
- C) The can bus is overloaded
- D) This is an expected result with the given accuracy of the sensors
- E) The endianness is wrong in the DAQ config
