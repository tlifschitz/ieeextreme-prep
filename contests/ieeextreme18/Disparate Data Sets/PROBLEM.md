# Disparate Data Sets

**IEEEXtreme 18.0** · Time limit: 500 ms · Memory limit: 256 MB

**CS Academy:** <https://csacademy.com/ieeextreme-practice/task/disparate-datasets/>

## *IEEE Xplore*

Warm greetings to all IEEExtreme Participants from the Xplore API Team!

As part of the IEEExtreme Competition, you will be tasked with a programming challenge to determine the topic of an academic journal. The input content file of this exercise is static (non-changing) to allow for consistent results during this competition.

For a full dynamic database search IEEE Xplore API is available for your IEEE research needs. Xplore API provides metadata on 4.9mm academic works and is now delivering full-text content on 50k 'Open Access' articles. Xplore API will make your research needs fast and easy. The Xplore API Portal supports PHP, Python and Java as well as providing output in JSON and XML formats. Many API use cases are listed within the API Portal.

Xplore API registration is free. To learn more about IEEE Xplore API please visit [https://developer.ieee.org/](https://developer.ieee.org/) and register for an API key TODAY!

## *Challenge*

Conferences can occur as stand-alone events or as part of a serialized set. There are two disparate data storages: the first one contains the serialized sets with their parents and the second one contains stand-alone events. Due to a wrong SQL script, they were mixed into one data storage containing all the records in a random order and with (possibly) some fields removed. The complete data has been provided in a CSV format containing all the events' records. Your task is to connect the parent events records to their serialized sets, fill in the missing data and exclude some events.

## Standard input

The input will contain CSV records with the parent events, serialized events and stand-alone events.

Records will take the following format:

`Event ID,"Event Title","Acronym",Project Code,3 Digit Project Code,"Record Type"`

- *Event ID* is a unique set of letters and numbers to identify each record.
- *Event Title* is the title of the event. Double quotes within the title will be escaped with standard CSV escape of two double quotes "". Example: “This is a ""test"" title”. If the input contains escaped double quotes then the output must contain the escaped double quotes. There could be more than one event with the same title, since some of them just use their parent event title. *All the titles will contain only printable ASCII characters*.
- *Acronyms* are assigned to the parent and the serialized events belonging to the set. When the acronym was assigned, there was no validation to determine if the acronym already existed. Therefore the acronym may not be unique across serialized sets.
- *Project Code* is a string containing letters and numbers assigned to each conference. It could be empty.
- *3 Digit Project Code* is the last three characters of the Project Code. This must be the same for all conferences in a serialized set.
- *Record Type* is either “Parent Event” or "IEEE Event".

The parent event has no Project Code or 3 Digit Project Code. If a parent event has children events, then its 3 Digit Project Code must updated to:

- `???`, if the children don't have the same 3 Digit Project Code, or
-  The 3 Digit Project Code of its children.

There are some conditions to exclude the events from the records, these are:

- Any parent event without children should be exclude from the output.
- All serialized sets that don't have a unique parent event should be eliminated from the output.
- Any record with no acronym is eliminated from the output.
- Any child event without a parent should be eliminated from the output.

Case is important when comparing acronyms. Rat, RAT, RaT, etc. are all different acronyms.

## Standard output

Print all the serialized sets sorted by acronym after applying the exclusion conditions. For each serialized set, print the parent event with its corresponding children afterwards. For each child record append the parent ID to the end of it as the samples show.

The parent must be the first record in each set followed by its children sorted lexicographically by title. If their titles are the same one, then compare their event IDs.

## Constraints and notes

- There will be at most $360$ records to read.

## Examples

### Example 1

Input:
```
a094x00000EXXzC,"IEEE International Conference on Autonomic Computing and Self-Organizing Systems","ACSOS",,,"Parent Event"
a094x00002MGty5,"2023 IEEE International Conference on Autonomic Computing and Self-Organizing Systems","ACSOS",23X51,X51,"IEEE Event"
a094x00001IYX7e,"2022 IEEE International Conference on Autonomic Computing and Self-Organizing Systems","ACSOS",22X51,X51,"IEEE Event"
a094x00000EXXrU,"Antennas Design and Measurement International Conference","acsos",,,"Parent Event"
a094x00000Bm112,"2021 Antennas Design and Measurement International Conference","acsos",21U43,U43,"IEEE Event"
a094x00000Bm0VM,"2019 Antennas Design and Measurement International Conference","acsos",19U43,U43,"IEEE Event"
a094x00000EXXzCxxx,"IEEE US Conference on Autonomic Computing and Self-Organizing Systems","1ACSOS",,,"Parent Event"
a094x00002MGty5xxx,"2023 IEEE US Conference on Autonomic Computing and Self-Organizing Systems","1ACSOS",23P00,P00,"IEEE Event"
a094x00000EXXzCyyy,"IEEE Conference on Autonomic Computing","bACSOS",,,"Parent Event"
a094x00002MGty5yyy,"2023 IEEE Conference on Autonomic Computing","bACSOS",23YN0,YN0,"IEEE Event"
a094x00000EXXrUxxx,"Antennas Design and Measurement US Conference","XYZ",,,"Parent Event"
a094x00002MGu5Nxxx,"1999 Antennas Design and Measurement Africa Conference","",23U43,U43,"IEEE Event"
```

Output:
```
a094x00000EXXzCxxx,"IEEE US Conference on Autonomic Computing and Self-Organizing Systems","1ACSOS",,P00,"Parent Event"
a094x00002MGty5xxx,"2023 IEEE US Conference on Autonomic Computing and Self-Organizing Systems","1ACSOS",23P00,P00,"IEEE Event",a094x00000EXXzCxxx
a094x00000EXXzC,"IEEE International Conference on Autonomic Computing and Self-Organizing Systems","ACSOS",,X51,"Parent Event"
a094x00001IYX7e,"2022 IEEE International Conference on Autonomic Computing and Self-Organizing Systems","ACSOS",22X51,X51,"IEEE Event",a094x00000EXXzC
a094x00002MGty5,"2023 IEEE International Conference on Autonomic Computing and Self-Organizing Systems","ACSOS",23X51,X51,"IEEE Event",a094x00000EXXzC
a094x00000EXXrU,"Antennas Design and Measurement International Conference","acsos",,U43,"Parent Event"
a094x00000Bm0VM,"2019 Antennas Design and Measurement International Conference","acsos",19U43,U43,"IEEE Event",a094x00000EXXrU
a094x00000Bm112,"2021 Antennas Design and Measurement International Conference","acsos",21U43,U43,"IEEE Event",a094x00000EXXrU
a094x00000EXXzCyyy,"IEEE Conference on Autonomic Computing","bACSOS",,YN0,"Parent Event"
a094x00002MGty5yyy,"2023 IEEE Conference on Autonomic Computing","bACSOS",23YN0,YN0,"IEEE Event",a094x00000EXXzCyyy
```

Explanation:

The excluded events' IDs are:

- `a094x00000EXXrUxxx`, since it doesn't have any children.
- `a094x00002MGu5Nxxx`, since it doesn't have a parent event.

### Example 2

Input:
```
a094x00000EXYC2,"IEEE Nanotechnology Symposium (ANTS)","ANTS",,,"Parent Event"
a094x00000Bm0iK,"2020 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)","ANTS",2069D,69D,"IEEE Event"
a094x00000Bm0uC,"2021 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)","ANTS",2169D,69D,"IEEE Event"
a094x00001IYXBs,"2022 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)","ANTS",2269D,69D,"IEEE Event"
a094x00000Bm0Hb,"2018 IEEE Nanotechnology Symposium (ANTS)","ANTS",18M86,M86,"IEEE Event"
a094x00000BlzyU,"2017 IEEE Nanotechnology Symposium (ANTS)","ANTS",17M86,M86,"IEEE Event"
a094x00000Bm01T,"2017 IEEE Australia New Zealand Student and Young Professional Congress (ANZSCON)","ANZSCON",17M74,M74,"IEEE Event"
a094x00000EXXtT,"IEEE Arctic and Northern Oceans Forum (ANOF)","ANOF",,,"Parent Event"
a094x00000Bm0U3,"2019 IEEE Arctic and Northern Oceans Forum (ANOF)","ANOF",19U27,U27,"IEEE Event"
a094x00000EXYG4,"IEEE Workshop on Animation in Virtual and Augmented Environments (ANIVAE)","ANIVAE",,,"Parent Event"
a094x00000Bm0CS,"2018 IEEE 1st Workshop on Animation in Virtual and Augmented Environments (ANIVAE)","ANIVAE",18P57,P57,"IEEE Event"
a094x00000Bm0TB,"2019 IEEE 2nd Workshop on Animation in Virtual and Augmented Environments (ANIVAE)","ANIVAE",19P57,P57,"IEEE Event"
a094x00000EXYG1,"IEEE Workshop on Advanced NeuroTechnologies for Brain Initiatives (ANTBI)","ANTBI",,,"Parent Event"
a094x00000EXXu2,"IEEE Brain Initiative Workshop on Advanced NeuroTechnologies for BRAIN Initiatives (ANTBI)","ANTBI",,,"Parent Event"
a094x00000Blzml,"2016 IEEE Workshop on Advanced NeuroTechnologies for Brain Initiatives (ANTBI)","ANTBI",16H29,H29,"IEEE Event"
```

Output:
```
a094x00000EXYG4,"IEEE Workshop on Animation in Virtual and Augmented Environments (ANIVAE)","ANIVAE",,P57,"Parent Event"
a094x00000Bm0CS,"2018 IEEE 1st Workshop on Animation in Virtual and Augmented Environments (ANIVAE)","ANIVAE",18P57,P57,"IEEE Event",a094x00000EXYG4
a094x00000Bm0TB,"2019 IEEE 2nd Workshop on Animation in Virtual and Augmented Environments (ANIVAE)","ANIVAE",19P57,P57,"IEEE Event",a094x00000EXYG4
a094x00000EXXtT,"IEEE Arctic and Northern Oceans Forum (ANOF)","ANOF",,U27,"Parent Event"
a094x00000Bm0U3,"2019 IEEE Arctic and Northern Oceans Forum (ANOF)","ANOF",19U27,U27,"IEEE Event",a094x00000EXXtT
a094x00000EXYC2,"IEEE Nanotechnology Symposium (ANTS)","ANTS",,???,"Parent Event"
a094x00000BlzyU,"2017 IEEE Nanotechnology Symposium (ANTS)","ANTS",17M86,M86,"IEEE Event",a094x00000EXYC2
a094x00000Bm0Hb,"2018 IEEE Nanotechnology Symposium (ANTS)","ANTS",18M86,M86,"IEEE Event",a094x00000EXYC2
a094x00000Bm0iK,"2020 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)","ANTS",2069D,69D,"IEEE Event",a094x00000EXYC2
a094x00000Bm0uC,"2021 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)","ANTS",2169D,69D,"IEEE Event",a094x00000EXYC2
a094x00001IYXBs,"2022 IEEE International Conference on Advanced Networks and Telecommunications Systems (ANTS)","ANTS",2269D,69D,"IEEE Event",a094x00000EXYC2
```

Explanation:

The excluded events' IDs are:

- `a094x00000Bm01T`, since it has no parent event.
- `a094x00000EXYG1`, `a094x00000EXXu2` and `a094x00000Blzml`, since the first two are both parent events and the latter must be excluded as well because it's their child.

Notice that the 3 Digit Project Code for event with ID `a094x00000EXYC2` is `???` since its children have two different 3 Digit Project Codes: `69D` and `M86`.
