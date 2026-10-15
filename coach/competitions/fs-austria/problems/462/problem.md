---
id: 462
event: "fs-austria"
year: 2022
rules_year: 2022
quizzes: [{"quiz_id": 43, "year": 2022, "class": "ev", "position": 9}, {"quiz_id": 44, "year": 2022, "class": "cv", "position": 9}]
type: "single-choice"
time_s: 300
topic: ["electronics"]
options: ["Node A, because Data Byte 0 has the higher value", "Node B, because Data Byte o has the lower value", "Node B, because the DLC has the lower value", "neither, this will cause a collision on the bus"]
answer: "neither, this will cause a collision on the bus"
unit: null
rule_refs: []
source: "https://fs-quiz.eu/question/462"
status: "unverified"
verified_by: null
---

# Problem 462

On your vehicles CAN network, two nodes have a message with the same ID queued:\n - Node A: ID 0x123, DLC 4, Date 0x55 0x55 0x55\n - Node B: ID 0x123, DLC 2, Date 0x00 0x00\n Both nodes start transmitting at the same time, which message will reach node C, which is setup to receive any 0x123 message, first if there is only a single attempt to transmit?

Options:
- A) Node A, because Data Byte 0 has the higher value
- B) Node B, because Data Byte o has the lower value
- C) Node B, because the DLC has the lower value
- D) neither, this will cause a collision on the bus
